function(doc) {

    // get current time.
    function getDate() {
	var dtNow = new Date();
	this.dtYear = dtNow.getFullYear();
	this.dtMon = dtNow.getMonth() + 1;
	this.dtMday = dtNow.getDate();
    };

    var date = new getDate();
    if(doc.thumbnail) {
	if ((doc.year == date.dtYear) && (doc.mon == date.dtMon) 
	    && (doc.mday == date.dtMday))
	    emit(doc.hour, doc);
    };
}