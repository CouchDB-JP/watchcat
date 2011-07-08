function (head, req) {
    start({
	"headers": {"Content-type":"text/html"}
    });
    var mustache = require("vendor/couchapp/lib/mustache");
    
    var datalist = [];
    var row;
    while (row = getRow()) {
	datalist.push({
	    _id: row.value._id,
	    thumbnail: row.value.thumbnail,
	    photo: row.value.photo,
	    year: row.value.year,
	    mon: row.value.mon,
	    mday: row.value.mday,
	    hour: row.value.hour,
	    min: row.value.min,
	    sec: row.value.sec
	});
    }
    var data = {"datalist":datalist,"hour":datalist[0].hour};
    return mustache.to_html(this.templates.hour, data);
}