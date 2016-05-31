var template = _.template($("#tree-template").html());

$('.person').selectize({
    valueField: 'id',
    labelField: 'name',
    searchField: ['name'],
    load: function(query, callback) {
        if (!query.length) return callback();
        $.ajax({
            url: '/search/' + encodeURIComponent(query),
            type: 'GET',
            error: function() {
                callback();
            },
            success: function(res) {
                callback(res.results);
            }
        });
    }
});

$('form').on('submit', function() {
    var personA = $('#person-a').val();
    var personB = $('#person-b').val();
    if (!(personA && personB)) {
        alert("Please select two people");
        return false;
    }
    if (personA === personB) {
        alert("Please select two different people");
        return false;
    }
    $.ajax('/relationship/' + personA + '/' + personB, {
        success: function(res) {
            $("#results").html(template(res));
        }
    });
    return false;
});

