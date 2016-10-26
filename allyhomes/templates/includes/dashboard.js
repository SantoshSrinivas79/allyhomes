// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ready(function() {	
	load_aging_so();
});

function load_aging_so(){	
//	kdemail = $('#kdselect').val();
//	kd_name = $('#kdselect').val();		
		frappe.call({
			type: "POST",
			method: "allyhomes.www.dashboard.get_aging_so",
			args: {
				
			},
			callback: function(r) {
				if(r.message){
					//console.log('object',r.message);
					item_html = '';
					$.each(r.message, function(i, currItem) {
						item_html +='<tr class="tr_custom"><td class="td_custom">'+currItem['item_code']+'</td><td class="td_custom">'+currItem['qty']+'</td></tr>';
					});
					$('#stock_level').html(item_html);
					
				}
				else
				{$('#stock_level').html('');}
			}
		
		})
}
