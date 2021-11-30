 $(document).ready(function () {
        console.log("ready!");
        buttonUpdate = $('.btn-update-event')
        console.log(buttonUpdate)
        buttonUpdate.click(function () {
            $('#dialog2').modal('show');
            var id = $(this).attr("event-id");
            $.ajax({
                url: `http://127.0.0.1:8000/api/v1/eventtest/${id}/`,
                method: 'get',
                data: { "id": id },
                dataType: 'json',
                contentType: "application/json",
                success: function (res) {
                    let eID = res.event_id
                    let eTitle = res.title
                    let eType = res.type
                    $("input[name=event_id]").val(eID);
                    $("input[name=event_title]").val(eTitle);
                    $("input[name=event_type]").val(eType);
                    $("#save-update-event").attr("eventid", res.event_id)
                },
                error: function (res) {
                    console.log(res)
                }
            });
        })
        function editEventABC(e) {
            $('#dialog2').modal('show');
            var id = $(e).attr("event-id");
            $.ajax({
                url: `http://127.0.0.1:8000/api/v1/eventtest/${id}`,
                method: 'get',
                data: { "id": id },
                dataType: 'json',
                contentType: "application/json",
                success: function (res) {
                    let eID = res.event_id
                    let eTitle = res.title
                    let eType = res.type
                    $("input[name=event_id]").val(eID);
                    $("input[name=event_title]").val(eTitle);
                    $("input[name=event_type]").val(eType);
                    $("#save-update-event").attr("eventid", res.event_id)
                },
                error: function (res) {
                    console.log(res)
                }
            });
        };

        var btnSaveUpdateEvent = $("#save-update-event")
        btnSaveUpdateEvent.click(function () {
            var ideventButton = $(this).attr("eventid");


            const id = $("input[name=event_id]").val();
            const title = $("input[name=event_title]").val();
            const type = $("input[name=event_type]").val();
            console.log(id)
            const datas = {
                "event_id": id,
                "title": title,
                "type": type
            }

            console.log(JSON.stringify(datas))
            $.ajax({
                url: `http://127.0.0.1:8000/api/v1/event/${id}/`,
                type: 'patch',
                data: JSON.stringify(datas),
                dataType: 'json',
                contentType: "application/json",
                success: function (res) {
                    alert('Update Thành Công');
                    window.location.reload();

                },
                error: function (res) {
                    alert('loi')
                }
            });
        })


        function deleteEvent(e) {
            var id = $(e).attr("id");

            if (confirm("Bạn chắc chắn muốn xóa")) {
                $.ajax({
                    url: `http://127.0.0.1:8000/api/v1/eventtest/${id}`,
                    method: 'delete',
                    data: { "id": id },
                    dataType: 'json',
                    contentType: "application/json",
                    success: function (res) {
                        console.log(res)
                        alert("Xóa thành công"); window.location.reload()
                    },
                    error: function (res) {
                        console.log(res)
                    }
                });
            }
        }
    });