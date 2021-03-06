var postApp = angular.module("postApp", ['ngRoute'])
    
postApp.config(function ($locationProvider, $httpProvider)
{
    $locationProvider.html5Mode(true);
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

postApp.controller("postController", function($scope, $http, $location, $window) {
    this.Init = function()
    {
         var postId = $location.search().id;
         if(!postId)
         {
            $window.location.href = 'post?id=1';
            return;
         }

         var responsePromise = $http(
         {
            url: "postdata/"+postId,
            method: "GET",
            headers: { "Accept": "application/json" }
         })

         responsePromise.success(function(data, status, headers, config) {
            $scope.postTitle = data.title;
            $scope.postDate = data.date;
            $scope.postContent = data.content;
            $scope.postAuthor = data.author;
         });
         responsePromise.error(function(data, status, headers, config) {
            alert("AJAX failed!");
         });
    }
    
    $scope.checkIfImg = function(part)
    {
        if(part.substring(0, "this_is_a_img_src".length)=="this_is_a_img_src")
            return true;
        else   
            return false;
    }
    
    this.Init();
});