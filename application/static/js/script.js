jQuery(document).ready(function () {

    $.datetimepicker.setLocale('ru');
    $('.datetimepicker').datetimepicker({
        onGenerate: function (ct) {
            $(this).find('.xdsoft_date.xdsoft_weekend')
                .addClass('xdsoft_disabled');
        },
        weekends: ['Сб', 'Вс'],
        dayOfWeekStart: "1",
        defaultDate: new Date(),
        defaultTime: '09:00',
        lang: 'ru',
        format: 'Y-m-d H:i',
        allowTimes: [
            '09:00', '10:00', '11:00', '12:00', '13:00',
            '14:00', '15:00', '16:00', '17:00', '18:00'
        ]
    });


    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        headers: {'X-Requested-With': 'XMLHttpRequest'}
    });

    $('#id_specialty')
        .change(function () {
            $.ajax({
                type: 'POST',
                url: '/update_specialists/',
                data: {'specialist_id': $(this).val()},
                success: function (data) {
                    $('#id_specialist').find('option').remove();
                    $('#id_specialist').append(
                        '<option value="" selected="selected">---------</option>');
                    $.each(data, function (key, value) {
                        $('#id_specialist').append(
                            '<option value=' + value.id + '>' + value.name_last +
                            ' ' + value.name_first + '</option>')
                    });
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    console.log(xhr.status);
                    console.log(thrownError);
                }
            });
        });
});