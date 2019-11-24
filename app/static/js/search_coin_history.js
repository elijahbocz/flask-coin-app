$('#search-history-button').click(function() {
  var date_input = $('#date_input').val();
  var coin_name = window.location.pathname.substring(8);

  url =
    'https://api.coingecko.com/api/v3/coins/' +
    coin_name +
    '/history?date=' +
    date_input;

  var settings = {
    async: true,
    crossDomain: true,
    url: url,
    method: 'GET',
    headers: {
      'cache-control': 'no-cache',
      'Postman-Token': 'fbc2c5b8-8b4d-4018-901e-1f905b8209cd'
    }
  };

  $.ajax(settings).done(function(response) {
    if (response['market_data'] != undefined) {
      var history_price = response['market_data']['current_price']['usd'];
      $('#history-result').text(
        'Approximate price on ' + date_input + ': $' + history_price.toFixed(8)
      );
    } else {
      $('#history-result').text('A price was not found for this date.');
    }
  });
});
