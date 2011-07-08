function (head, req) {
    start({
	"headers": {"Content-type":"text/html"}
    });
    var mustache = require("vendor/couchapp/lib/mustache");
    
    var datalist = [];
    var row;
    while (row = getRow()) {
	datalist.push({
	    year: row.key[0],
	    mon: row.key[1],
	    mday: row.key[2],
	    hour: row.key[3],
	    num: row.value
	});
    }
    var data = {"datalist":datalist};
    return mustache.to_html(this.templates.hours, data);
}