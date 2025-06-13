from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']  # 列表顯示的欄位
    list_filter = ['category', 'created_at']           # 過濾器
    search_fields = ['title', 'content']              # 搜尋欄位
    date_hierarchy = 'created_at'                     # 日期導航