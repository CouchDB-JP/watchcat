function (doc, req) {
    start({
	"headers":{
	    "Content-type":"text/html"
	}
    });

    var mustache = require("vendor/couchapp/lib/mustache");

    data = {
	_id: doc._id,
	photo: doc.photo,
	year: doc.year,
	mon: doc.mon,
	mday: doc.mday,
	hour: doc.hour,
	min: doc.min,
	sec: doc.sec
    };
    return mustache.to_html(this.templates.photo, data);
}