setInterval(function(){
    getData();
}, 5000);
function getData(){
    $.ajax({
        type: "GET",
        url: "assets/php/fetchStatus.php",
        data: "",
        cache: false,
        async: false,
        dataType: "json",
        success: function(data) {
            update(data.h);
            update(data.k);
            update(data.p);
        }
    });
}
function toggle(e, i){
    $('#'+e+'_available').hide();
    $('#'+e+'_idle').hide();
    $('#'+e+'_operational').hide();
    $('#'+e+'_computing').hide();
    $('#'+e+'_error').hide();
    $('#'+e+i).show();
}
function changeBackdrop(e, i) {
    $("#"+e).css('background-color', i);
    $("#"+e).css('boxShadow', 'inset 5px 5px 5px rgba(0,0,0,0.05), inset -5px 5px 5px rgba(255,255,255,0.5), 5px 5px 5px rgba(0,0,0,0.05), -5px -5px 5px rgba(255,255,255,0.5)');
}
function update(e){
    if((e.state).includes("Offline")){
        toggle(e.firstLetter, '_available');
        changeBackdrop(e.firstLetter, "#ebf5fc");
    }
    else if((e.state).includes("Detecting")){
        toggle(e.firstLetter, '_computing');
        changeBackdrop(e.firstLetter, "#ffcd01");
    }
    else{
        switch(e.state) {
            case 'Operational':
                toggle(e.firstLetter, '_idle');
                changeBackdrop(e.firstLetter, "#ffcd01");
                break;
            case 'Printing':
                toggle(e.firstLetter, '_operational');
                $('#'+e.firstLetter+'_time_left').text((parseInt(e.printTimeLeft)/3600).toFixed(2));
                $('#'+e.firstLetter+'_time_passed').text((parseInt(e.printTime)/3600).toFixed(2));
                $('#'+e.firstLetter+'_progress').text(((parseInt(e.printTime)/(parseInt(e.printTime)+parseInt(e.printTimeLeft)))*100).toFixed(1));
                $('#'+e.firstLetter+'_n_temp').text(e.nozzleTemp);
                $('#'+e.firstLetter+'_n_temp_target').text(e.nozzleTempTarget);
                $('#'+e.firstLetter+'_b_temp').text(e.bedTemp);
                $('#'+e.firstLetter+'_b_temp_target').text(e.bedTempTarget);
                changeBackdrop(e.firstLetter, "#02b875");
                break;
            case 'Cancelling':
                toggle(e.firstLetter, '_computing');
                changeBackdrop(e.firstLetter, "#ffcd01");
                break;
            default:
                toggle(e.firstLetter, '_error');
                changeBackdrop(e.firstLetter, "#000");
        }
    }
}