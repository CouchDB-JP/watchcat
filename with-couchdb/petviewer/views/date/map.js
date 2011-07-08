function(doc) {
    if (doc.type == "date") {
	var arrayDate = [doc.year, doc.mon, doc.mday, doc.hour];
	emit(arrayDate, 1);
    }
}