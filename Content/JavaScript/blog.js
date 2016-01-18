var blogApp = angular.module("blogApp",  ['infinite-scroll']);
//To limit the scroll exec delta time.
angular.module('infinite-scroll').value('THROTTLE_MILLISECONDS', 250);

blogApp.config(function ($httpProvider)
{
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

blogApp.factory('Overview', function($http)
{
    var Overview = function()
    {
        this.postsOverviewData =new Array();
        this.busy = false;
        this.hasMoreData = true;
        this.earliestDate = GetTomorrowDate();
        this.dupVerification = {};
    };
    
    Overview.prototype.loadMore = function() 
    {
        if (this.busy || !this.hasMoreData) return;
        this.busy = true; 
        //Fire the Ajax call to server to fetch the posts overview info.      
        var responsePromise = $http(
         {
            url: "getPostsOverviewBeforeDate?"+"date="+this.earliestDate+"&"+"numOfPost=5",
            method: "GET",
            headers: { "Accept": "application/json" }
         })

         responsePromise.success(function(data, status, headers, config) {
            if(status==404 || status == 206)
            {
                 //404:No more posts to fetch. 206: partially found.
                 this.hasMoreData=false;
            }
            
            //Check if data retrived has data in it. 
            if(data==undefined || data.length==0)
            {
                console.log("No Data fetched!");
                return;
            }
                
            var earliestDateInData = null;
            for(var i = 0; i < data.length; i++) 
            {
                var onePostOverview = data[i];
                //Check duplicate data.
                if(this.dupVerification[onePostOverview.postId]!=undefined)
                {
                    console.log("duplicate post overview received from server, postId= "+onePostOverview.postId);
                    return;
                }
                
                this.dupVerification[onePostOverview.postId] = onePostOverview;
                //Find the most recent post and record its date.            
                if(earliestDateInData==null || (ConstructDate(onePostOverview.postDate) < ConstructDate(earliestDateInData)))
                {
                    earliestDateInData = onePostOverview.postDate;
                }
                
                //Put post overview into the list of posts overview for ng-repeat to display.
                this.postsOverviewData.push(onePostOverview);
            }
            
            //Update the global most recent date among all the posts.
            if(ConstructDate(earliestDateInData) < ConstructDate(this.earliestDate))
            {
                this.earliestDate = earliestDateInData;
            }
            else
            {
                console.log("Data returned doesn't have posts ealier than what already retrived before!");
            }
            
            //Sort the overview of posts based on time, first is the most recent post.
            this.postsOverviewData.sort(function(o1,o2){
                return new Date(o1.postDate) - new Date(o2.postDate);
            });
            
            this.busy = false;                 
         }.bind(this));
         
         responsePromise.error(function(data, status, headers, config) {
            alert("Fetching post data from server failed. Server says:"+status+data);
         });
    }
    
    return Overview;
});

blogApp.controller("blogPostController", function($scope, $http, Overview) {
    var self = this;
    $scope.overview = new Overview();
    self.Init = function()
    {
        $scope.overview.loadMore();
    }
});

function GetTomorrowDate()
{
    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    var dd = tomorrow.getDate();
    var mm = tomorrow.getMonth()+1; //January is 0!
    var yyyy = tomorrow.getFullYear();

    if(dd<10) {
        dd='0'+dd
    }

    if(mm<10) {
        mm='0'+mm
    }

    tomorrow = mm+'/'+dd+'/'+yyyy;
    return tomorrow;
};

function ConstructDate(data)
{
    //dateFormat: mm/dd/yyyy
    var dateInfo = data.split("/");
    var month =dateInfo[0];
    var day = dateInfo[1];
    var year = dateInfo[2];
    var dateExtracted = new Date(year,month-1,day); //Jan is 0!
    return dateExtracted;
};

