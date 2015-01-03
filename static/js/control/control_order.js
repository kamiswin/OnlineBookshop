$(document).ready(function() {
    var numbers = $('span#item-number');
    var book_numbers = $('input#book-number');
    function calculateTotalPrice() {
        var total_price = 0
        $('input#item').each(function(index) {
            console.log($(this));
            if($(this).prop('checked')) {
                console.log(numbers.get(index));
                total_price += parseFloat($(this).val()) * parseInt(numbers.get(index).innerHTML);
            }
        });
        return total_price;
    }

    function showTotalPrice(val) {
        $('span.total-price').text(val);
    }
    $('input#item').on('click', function() {
        showTotalPrice(calculateTotalPrice());
    });


    $('button#controls-number-button-minus').each(function(index) {
        $(this).bind('click', function(event) { 
            event.preventDefault();
            var tn = parseInt(numbers[index].innerHTML);
            if(tn >= 1) {
                numbers[index].innerHTML = tn - 1;
                $('input#book-number' + index).val(tn - 1);
            }
            showTotalPrice(calculateTotalPrice());
        });
    });

    $('button#controls-number-button-add').each(function(index) { 
        $(this).bind('click', function(event) { 
            event.preventDefault();
            var tn = parseInt(numbers[index].innerHTML) + 1;
            numbers[index].innerHTML = tn;
            $('input#book-number' + index).val(tn);
            showTotalPrice(calculateTotalPrice());
        });
    });

    showTotalPrice(calculateTotalPrice());
});
