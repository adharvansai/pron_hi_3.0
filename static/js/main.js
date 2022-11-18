$(document).ready(function(){
    $('.rp_form').on('submit', function(e){
        // alert("test");
        const source = document.getElementById("source").value;
        $.ajax({
            url: '/report',
            method : "POST", 
            type: "POST", 
            data : {
                source: source,
                name:$('#rp_name').val(),
                message:$("#rp_msg").val()
            },
            success: function(){
                // alert("Success");
                const name = document.getElementById('rp_name');
                name.value = '';
                const msg = document.getElementById('rp_msg');
                msg.value = '';
                const ack = document.getElementById("rp_ack")
                ack.textContent = 'Thanks for reporting the issue and letting us improve!';
            }
        })
        e.preventDefault();

    });

    $('.fb_form').on('submit', function(e){
        // alert("test");
        const source = document.getElementById("source").value;
        $.ajax({
            url: '/feedback',
            method : "POST", 
            type: "POST", 
            data : {
                source: source,
                name:$('#fb_name').val(),
                email:$('#fb_email').val(),
                message:$("#fb_msg").val()
            },
            success: function(){
                // alert("Success");
                const name = document.getElementById('fb_name');
                name.value = '';
                const email = document.getElementById('fb_email');
                email.value = '';
                const msg = document.getElementById('fb_msg');
                msg.value = '';
                const ack = document.getElementById("fb_ack")
                ack.textContent = 'Thanks for providing your feedback!';
            }
        })
        e.preventDefault();

    });


})