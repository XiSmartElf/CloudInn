var blogApp = angular.module("blogApp", ['ngRoute'])
postApp.config(function ($locationProvider, $httpProvider)
{
    $locationProvider.html5Mode(true);
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

postApp.controller("blogPostController", function($scope, $http, $location, $window) {
    $scope.PostsOverviewData{};
    $scope.numOfPostLoaded = 0;
    this.Init = function()
    {
         var responsePromise = $http(
         {
            url: "getPostsOverview?"+,
            method: "GET",
            headers: { "Accept": "application/json" }
         })

         responsePromise.success(function(data, status, headers, config) {
            $scope.postData=data;
            $scope.postTitle = data.title;
            $scope.postDate = data.date;
            $scope.postText = data.text;
         });
         responsePromise.error(function(data, status, headers, config) {
            alert("AJAX failed!");
         });

    }

    this.Init();
});