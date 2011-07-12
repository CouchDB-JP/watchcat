$(function() {
    if (window.location.pathname.match("_design")) {
	var path = '../../index.html';
    } else {
	var path = '../../';
    }
    console.log(path);
    $('a#home').attr('href', path);	
});