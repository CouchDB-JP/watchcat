function(doc) {
    if (doc.photo) {
	var arrayDate = [doc.year, doc.mon, doc.mday, doc.hour];
	emit(arrayDate, 1);
    }
}