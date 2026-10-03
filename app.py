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
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QStackedWidget,
    QHeaderView,
    QSizePolicy
)
from PySide6.QtCore import Qt


class SecurityMonitor(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sentinel Linux Security Monitor")
        self.resize(1200, 750)

        self.setup_ui()
        self.apply_style()

    # --------------------------------------------------
    # MAIN UI
    # --------------------------------------------------

    def setup_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ==============================
        # SIDEBAR
        # ==============================

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(20, 25, 20, 20)
        sidebar_layout.setSpacing(10)

        logo = QLabel("🛡️  SENTINEL")
        logo.setObjectName("logo")

        logo_subtitle = QLabel("Linux Security Monitor")
        logo_subtitle.setObjectName("logoSubtitle")

        sidebar_layout.addWidget(logo)
        sidebar_layout.addWidget(logo_subtitle)

        sidebar_layout.addSpacing(30)

        self.dashboard_btn = self.create_nav_button(
            "▣   Dashboard"
        )

        self.events_btn = self.create_nav_button(
            "⚠   Security Events"
        )

        self.ip_btn = self.create_nav_button(
            "◎   IP Analysis"
        )

        self.reports_btn = self.create_nav_button(
            "▤   Reports"
        )

        self.monitor_btn = self.create_nav_button(
            "◉   Live Monitor"
        )

        self.settings_btn = self.create_nav_button(
            "⚙   Settings"
        )

        sidebar_layout.addWidget(self.dashboard_btn)
        sidebar_layout.addWidget(self.events_btn)
        sidebar_layout.addWidget(self.ip_btn)
        sidebar_layout.addWidget(self.reports_btn)
        sidebar_layout.addWidget(self.monitor_btn)

        sidebar_layout.addStretch()

        sidebar_layout.addWidget(self.settings_btn)

        version = QLabel("Sentinel v1.0")
        version.setObjectName("version")

        sidebar_layout.addWidget(version)

        main_layout.addWidget(sidebar)

        # ==============================
        # CONTENT AREA
        # ==============================

        content = QFrame()
        content.setObjectName("content")

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(35, 30, 35, 25)

        # Header

        header_layout = QHBoxLayout()

        header_text = QVBoxLayout()

        title = QLabel("Security Dashboard")
        title.setObjectName("pageTitle")

        subtitle = QLabel(
            "Linux authentication monitoring and threat detection"
        )
        subtitle.setObjectName("pageSubtitle")

        header_text.addWidget(title)
        header_text.addWidget(subtitle)

        header_layout.addLayout(header_text)
        header_layout.addStretch()

        status = QLabel("●  SYSTEM ONLINE")
        status.setObjectName("onlineStatus")

        header_layout.addWidget(status)

        content_layout.addLayout(header_layout)

        # ==============================
        # STACKED PAGES
        # ==============================

        self.pages = QStackedWidget()

        self.dashboard_page = self.create_dashboard_page()
        self.events_page = self.create_events_page()
        self.ip_page = self.create_ip_page()
        self.reports_page = self.create_reports_page()
        self.monitor_page = self.create_monitor_page()
        self.settings_page = self.create_settings_page()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.events_page)
        self.pages.addWidget(self.ip_page)
        self.pages.addWidget(self.reports_page)
        self.pages.addWidget(self.monitor_page)
        self.pages.addWidget(self.settings_page)

        content_layout.addWidget(self.pages)

        main_layout.addWidget(content)

        # Navigation

        self.dashboard_btn.clicked.connect(
            lambda: self.show_page(0)
        )

        self.events_btn.clicked.connect(
            lambda: self.show_page(1)
        )

        self.ip_btn.clicked.connect(
            lambda: self.show_page(2)
        )

        self.reports_btn.clicked.connect(
            lambda: self.show_page(3)
        )

        self.monitor_btn.clicked.connect(
            lambda: self.show_page(4)
        )

        self.settings_btn.clicked.connect(
            lambda: self.show_page(5)
        )

    # --------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------

    def create_dashboard_page(self):

        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)

        # Statistics

        cards = QGridLayout()
        cards.setSpacing(15)

        cards.addWidget(
            self.create_stat_card(
                "FAILED ATTEMPTS",
                "0",
                "Authentication failures"
            ),
            0, 0
        )

        cards.addWidget(
            self.create_stat_card(
                "SUSPICIOUS IPs",
                "0",
                "Unique source addresses"
            ),
            0, 1
        )

        cards.addWidget(
            self.create_stat_card(
                "HIGH RISK",
                "0",
                "Critical security events"
            ),
            0, 2
        )

        cards.addWidget(
            self.create_stat_card(
                "MONITOR",
                "READY",
                "Detection engine status"
            ),
            0, 3
        )

        layout.addLayout(cards)

        # Middle section

        middle = QHBoxLayout()
        middle.setSpacing(15)

        activity = QFrame()
        activity.setObjectName("panel")

        activity_layout = QVBoxLayout(activity)

        activity_title = QLabel("Attack Activity")
        activity_title.setObjectName("panelTitle")

        activity_info = QLabel(
            "Real-time authentication activity will appear here."
        )
        activity_info.setObjectName("mutedText")

        activity_layout.addWidget(activity_title)
        activity_layout.addSpacing(20)
        activity_layout.addWidget(activity_info)

        activity_layout.addStretch()

        middle.addWidget(activity, 2)

        alert = QFrame()
        alert.setObjectName("alertPanel")

        alert_layout = QVBoxLayout(alert)

        alert_title = QLabel("🚨 Security Status")
        alert_title.setObjectName("panelTitle")

        alert_text = QLabel(
            "No active threats detected."
        )
        alert_text.setObjectName("alertText")

        alert_layout.addWidget(alert_title)
        alert_layout.addSpacing(15)
        alert_layout.addWidget(alert_text)
        alert_layout.addStretch()

        middle.addWidget(alert, 1)

        layout.addLayout(middle)

        # Events

        events_title = QLabel("Recent Security Events")
        events_title.setObjectName("sectionTitle")

        layout.addWidget(events_title)

        table = self.create_event_table()

        layout.addWidget(table)

        return page

    # --------------------------------------------------
    # EVENT TABLE
    # --------------------------------------------------

    def create_event_table(self):

        table = QTableWidget(0, 5)

        table.setHorizontalHeaderLabels([
            "TIME",
            "USERNAME",
            "IP ADDRESS",
            "ATTEMPTS",
            "RISK"
        ])

        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        table.setMinimumHeight(180)

        table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        table.setAlternatingRowColors(False)

        return table

    # --------------------------------------------------
    # EVENTS PAGE
    # --------------------------------------------------

    def create_events_page(self):

        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("Security Events")
        title.setObjectName("sectionTitle")

        description = QLabel(
            "Detected failed authentication activity."
        )
        description.setObjectName("mutedText")

        table = self.create_event_table()

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(10)
        layout.addWidget(table)

        return page

    # --------------------------------------------------
    # IP PAGE
    # --------------------------------------------------

    def create_ip_page(self):

        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("IP Analysis")
        title.setObjectName("sectionTitle")

        description = QLabel(
            "Analyze source IP addresses associated with failed logins."
        )
        description.setObjectName("mutedText")

        ip_table = QTableWidget(0, 4)

        ip_table.setHorizontalHeaderLabels([
            "IP ADDRESS",
            "ATTEMPTS",
            "RISK",
            "STATUS"
        ])

        ip_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        ip_table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(10)
        layout.addWidget(ip_table)

        return page

    # --------------------------------------------------
    # REPORT PAGE
    # --------------------------------------------------

    def create_reports_page(self):

        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("Security Reports")
        title.setObjectName("sectionTitle")

        description = QLabel(
            "Generate and review security analysis reports."
        )
        description.setObjectName("mutedText")

        report = QFrame()
        report.setObjectName("panel")

        report_layout = QVBoxLayout(report)

        report_title = QLabel(
            "CSV Security Report"
        )
        report_title.setObjectName("panelTitle")

        report_status = QLabel(
            "security_report.csv"
        )
        report_status.setObjectName("mutedText")

        generate = QPushButton(
            "▤   GENERATE REPORT"
        )

        generate.setObjectName("primaryButton")

        report_layout.addWidget(report_title)
        report_layout.addWidget(report_status)
        report_layout.addSpacing(15)
        report_layout.addWidget(generate)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(20)
        layout.addWidget(report)
        layout.addStretch()

        return page

    # --------------------------------------------------
    # MONITOR PAGE
    # --------------------------------------------------

    def create_monitor_page(self):

        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("Live Monitor")
        title.setObjectName("sectionTitle")

        description = QLabel(
            "Continuous monitoring of Linux SSH authentication events."
        )
        description.setObjectName("mutedText")

        monitor_panel = QFrame()
        monitor_panel.setObjectName("panel")

        monitor_layout = QVBoxLayout(monitor_panel)

        status = QLabel(
            "● Monitoring engine ready"
        )
        status.setObjectName("monitorStatus")

        start = QPushButton(
            "▶   START MONITORING"
        )

        start.setObjectName("primaryButton")

        monitor_layout.addWidget(status)
        monitor_layout.addSpacing(20)
        monitor_layout.addWidget(start)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(20)
        layout.addWidget(monitor_panel)
        layout.addStretch()

        return page

    # --------------------------------------------------
    # SETTINGS PAGE
    # --------------------------------------------------

    def create_settings_page(self):

        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("Settings")
        title.setObjectName("sectionTitle")

        description = QLabel(
            "Security monitor configuration."
        )
        description.setObjectName("mutedText")

        settings = QFrame()
        settings.setObjectName("panel")

        settings_layout = QVBoxLayout(settings)

        info = QLabel(
            "Detection Engine\n\n"
            "Log source: systemd journal\n"
            "Service: SSH\n"
            "Risk engine: Enabled"
        )

        info.setObjectName("settingsText")

        settings_layout.addWidget(info)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(20)
        layout.addWidget(settings)
        layout.addStretch()

        return page

    # --------------------------------------------------
    # COMPONENTS
    # --------------------------------------------------

    def create_nav_button(self, text):

        button = QPushButton(text)

        button.setObjectName("navButton")

        button.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )

        return button

    def create_stat_card(self, title, value, description):

        card = QFrame()
        card.setObjectName("statCard")

        layout = QVBoxLayout(card)

        title_label = QLabel(title)
        title_label.setObjectName("cardTitle")

        value_label = QLabel(value)
        value_label.setObjectName("cardValue")

        description_label = QLabel(description)
        description_label.setObjectName("cardDescription")

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(description_label)

        return card

    # --------------------------------------------------
    # PAGE NAVIGATION
    # --------------------------------------------------

    def show_page(self, index):

        self.pages.setCurrentIndex(index)

    # --------------------------------------------------
    # STYLE
    # --------------------------------------------------

    def apply_style(self):

        self.setStyleSheet("""

            QMainWindow {
                background-color: #0b0f14;
            }

            QWidget {
                background-color: #0b0f14;
                color: #e6edf3;
                font-family: Arial;
            }

            /* SIDEBAR */

            QFrame#sidebar {
                background-color: #11161d;
                border-right: 1px solid #242b35;
            }

            QLabel#logo {
                color: #58a6ff;
                font-size: 22px;
                font-weight: bold;
            }

            QLabel#logoSubtitle {
                color: #6e7681;
                font-size: 11px;
            }

            QLabel#version {
                color: #484f58;
                font-size: 11px;
            }

            QPushButton#navButton {
                background-color: transparent;
                color: #8b949e;
                border: none;
                text-align: left;
                padding: 13px;
                border-radius: 7px;
                font-size: 13px;
            }

            QPushButton#navButton:hover {
                background-color: #1c2530;
                color: #e6edf3;
            }

            /* CONTENT */

            QFrame#content {
                background-color: #0b0f14;
            }

            QLabel#pageTitle {
                font-size: 28px;
                font-weight: bold;
                color: #f0f6fc;
            }

            QLabel#pageSubtitle {
                color: #7d8590;
                font-size: 13px;
            }

            QLabel#onlineStatus {
                color: #3fb950;
                font-size: 12px;
                font-weight: bold;
                padding: 8px 12px;
                background-color: #12251a;
                border-radius: 6px;
            }

            /* CARDS */

            QFrame#statCard {
                background-color: #11161d;
                border: 1px solid #242b35;
                border-radius: 10px;
                min-height: 120px;
            }

            QLabel#cardTitle {
                color: #7d8590;
                font-size: 11px;
                font-weight: bold;
            }

            QLabel#cardValue {
                color: #58a6ff;
                font-size: 27px;
                font-weight: bold;
            }

            QLabel#cardDescription {
                color: #484f58;
                font-size: 10px;
            }

            /* PANELS */

            QFrame#panel {
                background-color: #11161d;
                border: 1px solid #242b35;
                border-radius: 10px;
            }

            QFrame#alertPanel {
                background-color: #171316;
                border: 1px solid #4d272d;
                border-radius: 10px;
            }

            QLabel#panelTitle {
                color: #e6edf3;
                font-size: 15px;
                font-weight: bold;
            }

            QLabel#sectionTitle {
                color: #e6edf3;
                font-size: 18px;
                font-weight: bold;
            }

            QLabel#mutedText {
                color: #7d8590;
                font-size: 12px;
            }

            QLabel#alertText {
                color: #8b949e;
                font-size: 13px;
            }

            QLabel#monitorStatus {
                color: #3fb950;
                font-size: 14px;
                font-weight: bold;
            }

            QLabel#settingsText {
                color: #8b949e;
                font-size: 13px;
                line-height: 1.5;
            }

            /* BUTTONS */

            QPushButton#primaryButton {
                background-color: #238636;
                color: white;
                border: none;
                border-radius: 7px;
                padding: 12px 18px;
                font-weight: bold;
            }

            QPushButton#primaryButton:hover {
                background-color: #2ea043;
            }

            /* TABLE */

            QTableWidget {
                background-color: #11161d;
                border: 1px solid #242b35;
                border-radius: 8px;
                gridline-color: #1c232d;
                color: #c9d1d9;
                selection-background-color: #1f3a56;
            }

            QHeaderView::section {
                background-color: #161b22;
                color: #7d8590;
                border: none;
                border-bottom: 1px solid #242b35;
                padding: 10px;
                font-size: 11px;
                font-weight: bold;
            }

            QTableWidget::item {
                padding: 8px;
            }

        """)


# --------------------------------------------------
# APPLICATION START
# --------------------------------------------------

app = QApplication(sys.argv)

window = SecurityMonitor()
window.show()

sys.exit(app.exec())
