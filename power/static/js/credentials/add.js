$(function(){

    var machine_fields = ['machine_ssh_username', 'machine_ssh_password', 'machine_confirm_ssh_password', 'machine_ssh_private_key', 'machine_key_password']
    var scm_fields = ['scm_username', 'scm_password', 'scm_private_key', 'scm_key_password'];
    var aws_fields = ['aws_access_key', 'aws_secret_key'];
    var openstack_fields = ['openstack_auth_url', 'openstack_access_key', 'openstack_secret_key'];

    var options = [
        {"value":"machine", "fields": machine_fields},
        {"value":"scm", "fields": scm_fields},
        {"value": "aws", "fields": aws_fields},
        {"value": "openstack", "fields": openstack_fields}
    ];

    function select_state_from($ele, options){
        var all_fields = [];
        for (index in options) {
            all_fields = all_fields.concat(options[index]['fields'])
        }

        hide_form_element(all_fields);

        $ele.change(function(){
            var value = $ele.val();
            if (value==""){
                return;
            }
            for (index in options){
                if (value == options[index]['value']){
                    show_form_element(all_fields, options[index]['fields'])
                }
            }
        });
    }

    function hide_form_element(fields) {
        for (index in fields) {
            var $field = $("#"+fields[index]);
            $field.hide();
            console.log($field);
        }
    }

    function show_form_element(all_fields, fields){
        hide_form_element(all_fields);
        for (i in fields){
            $("#"+fields[i]).show();
        }
    }

    select_state_from($('#type'), options);

});