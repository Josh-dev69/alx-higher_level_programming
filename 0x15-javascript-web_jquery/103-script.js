document.addEventListener('DOMContentLoaded', function () {
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function (e) {
        if (e.which === 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        const languageCode = $('#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

        $.ajax({
            url: apiUrl,
            success: function (data) {
                const helloMessage = data.hello;
                $('#hello').text(helloMessage);
            },
            error: function () {
                $('#hello').text('Error fetching translation');
            }
        });
    }
});
