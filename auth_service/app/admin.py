# Register your models here.
from django.contrib import admin
from .models import UserCus, RoleCus

class UserCusAdmin(admin.ModelAdmin):
    # Hiển thị các trường trong danh sách Admin
    list_display = ('id', 'fullname', 'username', 'email', 'created_at', 'isActive', 'role', 'password')

    # Cho phép tìm kiếm theo email và username
    search_fields = ('email', 'username', 'fullname')

    # Cho phép lọc theo vai trò (role)
    list_filter = ('role',)

    # Sắp xếp theo 'created_at' (từ mới nhất)
    ordering = ('-created_at',)

admin.site.register(UserCus, UserCusAdmin)



class RoleCusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Thêm 'id' vào list_display
admin.site.register(RoleCus, RoleCusAdmin)