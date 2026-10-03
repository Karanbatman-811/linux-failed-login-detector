import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame
)
from PySide6.QtCore import Qt


class SecurityMonitor(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Linux Security Monitor")
        self.setMinimumSize(1000, 650)

        # Main widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # =========================
        # HEADER
        # =========================

        title = QLabel("🛡️  Linux Security Monitor")
        title.setObjectName("title")

        subtitle = QLabel(
            "Failed Login Detection & Security Analysis"
        )
        subtitle.setObjectName("subtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # =========================
        # DASHBOARD CARDS
        # =========================

        cards_layout = QGridLayout()

        self.failed_card = self.create_card(
            "FAILED ATTEMPTS",
            "0"
        )

        self.ip_card = self.create_card(
            "SUSPICIOUS IPs",
            "0"
        )

        self.high_card = self.create_card(
            "HIGH RISK EVENTS",
            "0"
        )

        self.status_card = self.create_card(
            "SYSTEM STATUS",
            "READY"
        )

        cards_layout.addWidget(self.failed_card, 0, 0)
        cards_layout.addWidget(self.ip_card, 0, 1)
        cards_layout.addWidget(self.high_card, 0, 2)
        cards_layout.addWidget(self.status_card, 0, 3)

        main_layout.addLayout(cards_layout)

        # =========================
        # ACTION BUTTONS
        # =========================

        buttons_layout = QHBoxLayout()

        scan_button = QPushButton("🔍  START SCAN")
        scan_button.setObjectName("primaryButton")

        report_button = QPushButton("📄  VIEW REPORT")
        report_button.setObjectName("secondaryButton")

        monitor_button = QPushButton("📡  LIVE MONITOR")
        monitor_button.setObjectName("secondaryButton")

        buttons_layout.addWidget(scan_button)
        buttons_layout.addWidget(report_button)
        buttons_layout.addWidget(monitor_button)

        main_layout.addLayout(buttons_layout)

        # =========================
        # SECURITY EVENTS
        # =========================

        events_title = QLabel("Recent Security Events")
        events_title.setObjectName("sectionTitle")

        main_layout.addWidget(events_title)

        events_box = QFrame()
        events_box.setObjectName("eventsBox")

        events_layout = QVBoxLayout()
        events_box.setLayout(events_layout)

        event = QLabel(
            "No security events detected yet."
        )
        event.setObjectName("eventText")

        events_layout.addWidget(event)

        main_layout.addWidget(events_box)

        # =========================
        # FOOTER
        # =========================

        footer = QLabel(
            "Linux Failed Login Detector  •  Python + PySide6"
        )
        footer.setAlignment(Qt.AlignCenter)
        footer.setObjectName("footer")

        main_layout.addWidget(footer)

        # =========================
        # BUTTON ACTION
        # =========================

        scan_button.clicked.connect(
            lambda: self.update_status("SCAN READY")
        )

        monitor_button.clicked.connect(
            lambda: self.update_status("MONITORING")
        )

        report_button.clicked.connect(
            lambda: self.update_status("REPORT READY")
        )

        # =========================
        # STYLE
        # =========================

        self.setStyleSheet("""
            QMainWindow {
                background-color: #0b0f14;
            }

            QWidget {
                background-color: #0b0f14;
                color: #e6edf3;
                font-family: Arial;
            }

            QLabel#title {
                font-size: 30px;
                font-weight: bold;
                color: #58a6ff;
                padding-top: 15px;
            }

            QLabel#subtitle {
                font-size: 15px;
                color: #8b949e;
                padding-bottom: 20px;
            }

            QFrame {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 10px;
            }

            QLabel#cardTitle {
                font-size: 13px;
                color: #8b949e;
            }

            QLabel#cardValue {
                font-size: 28px;
                font-weight: bold;
                color: #58a6ff;
            }

            QPushButton {
                padding: 14px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton#primaryButton {
                background-color: #238636;
                color: white;
                border: none;
            }

            QPushButton#secondaryButton {
                background-color: #21262d;
                color: #e6edf3;
                border: 1px solid #30363d;
            }

            QLabel#sectionTitle {
                font-size: 20px;
                font-weight: bold;
                padding-top: 20px;
                padding-bottom: 10px;
            }

            QFrame#eventsBox {
                min-height: 120px;
                padding: 10px;
            }

            QLabel#eventText {
                color: #8b949e;
                font-size: 14px;
            }

            QLabel#footer {
                color: #6e7681;
                padding-top: 15px;
            }
        """)

    def create_card(self, title, value):

        card = QFrame()
        card.setMinimumHeight(120)

        layout = QVBoxLayout()
        card.setLayout(layout)

        title_label = QLabel(title)
        title_label.setObjectName("cardTitle")

        value_label = QLabel(value)
        value_label.setObjectName("cardValue")

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        return card

    def update_status(self, status):

        self.status_card.findChildren(QLabel)[1].setText(status)


# =========================
# START APPLICATION
# =========================

app = QApplication(sys.argv)

window = SecurityMonitor()
window.show()

sys.exit(app.exec())
