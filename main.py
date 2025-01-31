import flet as ft
from flet import *
import webbrowser
import os
import time
from datetime import datetime
import json

class AppMonitor:
    def __init__(self):
        self.apps_list = []
        self.is_monitoring = False
        ft.app(target=self.main)

    def open_usage_settings(self):
        """فتح إعدادات الوصول للتطبيق"""
        try:
            os.system('am start -a android.settings.USAGE_ACCESS_SETTINGS')
        except:
            print("غير قادر على فتح الإعدادات")

    def save_app_data(self, app_name, start_time):
        """حفظ بيانات التطبيق"""
        data = {
            'app_name': app_name,
            'start_time': start_time,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open('app_history.json', 'a') as f:
                json.dump(data, f)
                f.write('\n')
        except Exception as e:
            print(f"خطأ في حفظ البيانات: {e}")

    def create_drawer(self):
        """إنشاء القائمة الجانبية"""
        return NavigationDrawer(
            controls=[
                Container(
                    content=Column([
                        Container(
                            content=Image(
                                src="assets/logo.png",
                                width=100,
                                height=100,
                                fit=ImageFit.CONTAIN,
                            ),
                            padding=padding.all(20),
                        ),
                        ListTile(
                            leading=Icon(ft.icons.INFO),
                            title=Text("حول التطبيق"),
                            subtitle=Text("الإصدار 1.0.0"),
                        ),
                        Divider(),
                        ListTile(
                            leading=Icon(ft.icons.PERSON),
                            title=Text("المطور"),
                            subtitle=Text("اسم المطور هنا"),
                        ),
                        ListTile(
                            leading=Icon(ft.icons.EMAIL),
                            title=Text("تواصل معنا"),
                            subtitle=Text("email@example.com"),
                            on_click=lambda _: webbrowser.open("mailto:email@example.com"),
                        ),
                        ListTile(
                            leading=Icon(ft.icons.PRIVACY_TIP),
                            title=Text("سياسة الخصوصية"),
                            on_click=lambda _: webbrowser.open("https://your-privacy-policy-url.com"),
                        ),
                        ListTile(
                            leading=Icon(ft.icons.STAR),
                            title=Text("قيم التطبيق"),
                            on_click=lambda _: webbrowser.open("https://play.google.com/store/apps/details?id=your.app.id"),
                        ),
                    ])
                )
            ]
        )

    def create_app_list_view(self):
        """إنشاء قائمة التطبيقات"""
        return ListView(
            expand=True,
            spacing=10,
            padding=20,
        )

    def main(self, page: ft.Page):
        # إعدادات الصفحة
        page.title = "مراقب التطبيقات"
        page.theme_mode = ThemeMode.DARK
        page.window_width = 400
        page.window_height = 800
        
        # إنشاء زر الوصول الرئيسي
        main_button = ElevatedButton(
            content=Container(
                content=Column([
                    Icon(
                        icons.APP_SETTINGS_ALT,
                        size=50,
                        color=colors.WHITE,
                    ),
                    Text(
                        "منح صلاحية الوصول",
                        size=20,
                        color=colors.WHITE,
                        text_align=TextAlign.CENTER,
                    )
                ]),
                padding=padding.all(20),
                alignment=alignment.center,
            ),
            style=ButtonStyle(
                shape=CircleBorder(),
                padding=padding.all(30),
                bgcolor={
                    MaterialState.DEFAULT: colors.BLUE,
                    MaterialState.HOVERED: colors.BLUE_700,
                },
                elevation={"pressed": 0, "": 10},
            ),
            on_click=lambda _: self.open_usage_settings()
        )

        # إنشاء القائمة الجانبية
        page.drawer = self.create_drawer()

        # زر فتح القائمة الجانبية
        menu_button = IconButton(
            icon=icons.MENU,
            on_click=lambda _: page.drawer.open()
        )

        # شريط العنوان
        page.appbar = AppBar(
            leading=menu_button,
            title=Text("مراقب التطبيقات"),
            center_title=True,
            bgcolor=colors.BLUE,
            actions=[
                IconButton(
                    icon=icons.HELP_OUTLINE,
                    on_click=lambda _: page.show_dialog(
                        AlertDialog(
                            title=Text("مساعدة"),
                            content=Text("1. اضغط على الزر للوصول إلى الإعدادات\n2. قم بتفعيل صلاحية الوصول للتطبيق\n3. عد إلى التطبيق لبدء المراقبة"),
                        )
                    )
                )
            ]
        )

        # مساحة الإعلان
        ad_banner = Container(
            content=Text(
                "مساحة مخصصة للإعلان",
                size=16,
                color=colors.WHITE,
                text_align=TextAlign.CENTER,
            ),
            bgcolor=colors.GREY_800,
            padding=padding.all(10),
            alignment=alignment.center,
            width=float("inf"),
            height=50,
        )

        # قائمة التطبيقات
        apps_list_view = self.create_app_list_view()

        # تنظيم عناصر الصفحة
        page.add(
            Column([
                Container(
                    content=main_button,
                    alignment=alignment.center,
                    expand=True,
                ),
                apps_list_view,
                ad_banner,
            ],
            alignment=MainAxisAlignment.BETWEEN,
            expand=True,
            )
        )

        # تحديث الصفحة
        page.update()

if __name__ == "__main__":
    AppMonitor()