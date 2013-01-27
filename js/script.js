/*global $,document */
/*jslint vars: true */
"use strict";
$(document).ready(function () {
    $.getJSON('overview.json', function (data) {
        //do stuff with overview data or whatever	
    });
    $.getJSON('list.json', function (data) {
        //print out the list of trusts
        var lists = [];
        var listone = "";
        var listtwo = "";
        var listthree = "";
        var listfour = "";

        $.each(data, function (key, value) {
            var linkStr = '<li><a class="' + key + '">' + value + '</a></li>';
            lists.push(linkStr);
        });
        var i;
        for (i = 0; i < lists.length; i += 1) {
            if (i % 4 === 0) {
                listone = listone + lists[i];
            } else if (i % 4 === 1) {
                listtwo = listtwo + lists[i];
            } else if (i % 4 === 2) {
                listthree = listthree + lists[i];
            } else if (i % 4 === 3) {
                listfour = listfour + lists[i];
            }
        }
        $(".trusts").html('<div class="span3"><ul>' + listone + '</ul></div><div class="span3"><ul>' + listtwo + '</ul></div><div class="span3"><ul>' + listthree + '</ul></div><div class="span3"><ul>' + listfour + '</ul></div>');



    });
    $(document).on("click", ".trusts ul li a", function (event) {
        event.preventDefault();
        var trustFilename = $(this).attr('class');
        var trustHTML = "";
        $.getJSON('output/' + trustFilename + '.json', function (data) {
            trustHTML = '<h1>' + data['name'] + '</h1>';
            trustHTML += '<dl class="dl-horizontal">';
            trustHTML += '<dt>Site URL</dt>';
            trustHTML += '<dd>' + data['site-url'] + '</dd>';
            trustHTML += '<dt>Doctype</dt>';
            trustHTML += '<dd>' + data['doctype'] + '</dd>';
            trustHTML += '<dt>Server</dt>';
            trustHTML += '<dd>' + data['headers']['server'] + '</dd>';
            trustHTML += '<dt>Framework</dt>';
            trustHTML += '<dd>' + data['headers']['poweredBy'] + '</dd>';
            trustHTML += '<dt>Uses humans.txt?</dt>';
            trustHTML += '<dd>' + data['humans'] + '</dd>';
            trustHTML += '<dt>Uses robots.txt?</dt>';
            trustHTML += '<dd>' + data['robots'] + '</dd>';
            trustHTML += '<dt>NHS Choices URL</dt>';
            trustHTML += '<dd>' + data['listing-url'] + '</dd>';
            trustHTML += '<dt>Has a sitemap available?</dt>';
            trustHTML += '<dd>' + data['sitemap'] + '</dd>';
            trustHTML += '<dt>Offers secure browsing (https)</dt>';
            trustHTML += '<dd>' + data['ssl'] + '</dd>';
            trustHTML += '</dl>';

            $.colorbox({
               html: trustHTML
            });
        });
    });
});
