$(function() {
   
    // function
    function Dates() {
	this.dtNow = new Date();
	this.dtMon = this.dtNow.getMonth() + 1;
	this.dtDate = this.dtNow.getDate();    
	this.dtHour = this.dtNow.getHours();
	this.dtMin = this.dtNow.getMinutes();
	this.dtSec = this.dtNow.getSeconds();
	if (this.dtMon < 10) this.dtMon = "0" + this.dtMon;
	if (this.dtDate < 10) this.dtDate = "0" + this.dtDate;
	this.strDate = this.dtNow.getFullYear() + "-" + this.dtMon + "-" + this.dtDate;
    }


    // generate hours list.
    var Dates = new Dates();
    // today
    if ($("ul#today")) {
	while (Dates.dtHour >= 0) {
	    $("ul#today")
		.append('<li><a href="" rel="external">' + Dates.dtHour + '時</a></li>');
	    --Dates.dtHour;
	}
    }
    // yesterday
    if ($("ul#yesterday")) {
	var i = 23;
	while (i >=0) {
	    $("ul#yesterday")
		.append('<li><a href="" rel="external">' + i + '時</a></li>');
	    --i;
	}
    }
    
});