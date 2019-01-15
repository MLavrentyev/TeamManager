
$(function() {
    var start = moment().subtract(29, 'days');
    var end = moment();

    function update(start, end) {
        $("#daterange").val(start.format('MMM D, YYYY') + ' - ' + end.format('MMM D, YYYY'));
    }

    $("#range-input").daterangepicker({
        startDate: start,
        endDate: end,
        ranges: {
            'Today': [moment(), moment()],
            'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Last 7 Days': [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment()],
            'This Year': [moment().startOf('year'), moment()],
            'All Time': [moment("{{ earliest_req }}"), moment()]
        }
    }, update);

});