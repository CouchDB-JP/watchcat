$(function() {
    
    function Dates() {
	this.dtNow = new Date();
	this.dtDate = this.dtNow.getDate();    
	this.dtHour = this.dtNow.getHours();
    }


    // generate hours list.
    var Dates = new Dates();
    // today
    if ($("ul#today")) {
	while (Dates.dtHour >= 0) {
	    $("ul#today")
		.append('<li><a href="_list/hour/today?key=' + Dates.dtHour + '">' + Dates.dtHour + '時</a></li>');
	    --Dates.dtHour;
	}
    }
    // yesterday
    if ($("ul#yesterday")) {
	var i = 23;
	while (i >=0) {
	    $("ul#yesterday")
		.append('<li><a href="_list/hour/yesterday?key=' + i + '">' + i + '時</a></li>');
	    --i;
	}
    }
    
});