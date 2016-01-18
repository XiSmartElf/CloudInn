var blogApp = angular.module("blogApp",  ['infinite-scroll'])
angular.module('infinite-scroll').value('THROTTLE_MILLISECONDS', 250)

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
        this.earliestDate = GetTodayDate();
        this.dupVerification = {};
    };
    
    Overview.prototype.loadMore = function() 
    {
        if (this.busy) return;
        this.busy = true;       
        var responsePromise = $http(
         {
            url: "getPostsOverviewBeforeDate?"+"date="+this.earliestDate+"&"+"numOfPost=5",
            method: "GET",
            headers: { "Accept": "application/json" }
         })

         responsePromise.success(function(data, status, headers, config) {
            var earliestDateInData = null;
            for(var i = 0; i < data.length; i++) 
            {
                var onePostOverview = data[i];
                onePostOverview.postDate = ConstructDate(onePostOverview.postDate);
                if(this.dupVerification[onePostOverview.postId]!=undefined)
                {
                    console.log("duplicate post overview received from server, postId= "+onePostOverview.postId);
                    return;
                }
                
                this.dupVerification[onePostOverview.postId] = onePostOverview;
                             
                if(earliestDateInData==null)
                {
                    earliestDateInData = onePostOverview.postDate;
                }
                else
                {
                    if(onePostOverview.postDate < earliestDateInData)
                    {
                        earliestDateInData = onePostOverview.postDate;
                    }
                }
                
                this.earliestDate = earliestDateInData;
                this.postsOverviewData.push(onePostOverview);
            }

            this.postsOverviewData.sort(function(o1,o2){
                return new Date(o1.postDate) - new Date(o2.postDate);
            });
            
            this.busy = false;                 
         }.bind(this));
         
         responsePromise.error(function(data, status, headers, config) {
            alert("AJAX failed!");
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

function GetTodayDate()
{
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
        dd='0'+dd
    }

    if(mm<10) {
        mm='0'+mm
    }

    today = mm+'/'+dd+'/'+yyyy;
    return today;
};

function ConstructDate(data)
{
    //dateFormat: mm/dd/yyyy
    var dateInfo = data.split("/");
    var month =dateInfo[0];
    var day = dateInfo[1];
    var year = dateInfo[2];
    var dateExtracted = new Date(year,month-1,day);
    return dateExtracted;
};

