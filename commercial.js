
let table = new DataTable('#myTable', {
    language: {
        url: "https://cdn.datatables.net/plug-ins/1.12.1/i18n/pt-BR.json"
    },
    initComplete: function () {
        this.api()
            .columns()
            .every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($(column.footer()).empty())
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex($(this).val());

                        column.search(val ? '^' + val + '$' : '', true, false).draw();
                    });

                column
                    .data()
                    .unique()
                    .sort()
                    .each(function (d, j) {
                        select.append('<option value="' + d + '">' + d + '</option>');
                    });
            });
    },

});

let myModal = document.getElementById('exampleModal')
myModal.addEventListener('shown.bs.modal', () => {
    myInput.focus()
})
myModal = new bootstrap.Modal(myModal)
myModal.show()

function updatePercentage() {
    const offer = Number(document.getElementById('offer').value);
    const updatedValue = Number(document.getElementById('updated_value').value)
    const percentage = Math.round(offer / updatedValue * 100)
    document.getElementById('percentage').innerText =
        isNaN(percentage) || !isFinite(percentage) ? "-" : `${percentage} %`;
}
