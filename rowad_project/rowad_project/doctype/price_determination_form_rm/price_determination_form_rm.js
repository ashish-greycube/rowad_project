// Copyright (c) 2024, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Price Determination Form RM", {
	total_costs(frm) {
        calculate_total_price(frm)
        calculate_vat(frm)
	},
    expected_profit(frm) {
        calculate_total_price(frm)
        
    },
    total_price(frm) {
        frm.set_value("vat_15",undefined)
        frm.set_value("total_price_with_vat",undefined)
        if(frm.doc.total_price) {
            frappe.db.get_single_value('Rowad Settings RM', 'vat_percentage')
            .then(vat_percentage => {
                console.log(vat_percentage);
                let vat_value = (frm.doc.total_price * vat_percentage)/100
                frm.set_value("vat_15",vat_value)
                let total_price_with_vat = frm.doc.total_price + frm.doc.vat_15
                frm.set_value("total_price_with_vat",total_price_with_vat)
            })
        }
    }
});

let calculate_total_price = function(frm) {
    let total_price = (frm.doc.total_costs || 0 )+ (frm.doc.expected_profit || 0)
    frm.set_value("total_price",total_price)
}

let calculate_vat = function(frm) {
    frappe.db.get_single_value('Rowad Settings RM', 'vat_percentage')
    .then(vat_percentage => {
        console.log(vat_percentage);
    })

}