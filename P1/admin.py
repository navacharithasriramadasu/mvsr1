from django.contrib import admin

import pandas as pd
from django.http import HttpResponse

# Register your models here.

from django.contrib import admin
from .models import *


admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Sem)
admin.site.register(Branch)
admin.site.register(Notifications)


@admin.action(description="Download selected payments as Excel")
def download_selected_payments(modeladmin, request, queryset):
    payments = queryset.values(
        "student__Rollno", "student__Name", "student__Branch","student__Semester", 
        "notification__notification", "amount_paid", "payment_status"
    )
    df = pd.DataFrame(payments)

    df.rename(columns={
        "student__Rollno": "Roll No",
        "student__Name": "Student Name",
        "student__Branch": "Branch",
        "student__Semester":"Semester",
        "notification__notification": "Notification",
        "amount_paid": "Amount Paid",
        "payment_status": "Payment Status",
    }, inplace=True)

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="selected_payments.xlsx"'

    with pd.ExcelWriter(response, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Payments")

    return response

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student", "notification", "amount_paid", "payment_status")
    search_fields = ("student__Rollno", "student__Name", "notification__notification")
    list_filter = ("payment_status",)
    actions = [download_selected_payments] 
