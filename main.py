from appium import webdriver


class WebDriver(
    AppiumSearchContext,
    ActionHelpers,
    Activities,
    Applications,
    Clipboard,
    Context,
    Common,
    DeviceTime,
    Display,
    ExecuteDriver,
    ExecuteMobileCommand,
    Gsm,
    HardwareActions,
    ImagesComparison,
    IME,
    Keyboard,
    Location,
    LogEvent,
    Network,
    Performance,
    Power,
    RemoteFS,
    ScreenRecord,
    Session,
    Settings,
    Sms,
    SystemBars,
):
    def __init__(
        self,
            platformName : "Android",
            platformVersion : "10",
            appium:deviceName : "dandelion_global ",
            appium:automationName : "UiAutomator1",
            appium:appPackage : "com.habitsv2",
            appium:appActivity : ".MainActivity"
    ):

        if strict_ssl is False:
            # pylint: disable=E1101
            import urllib3

            AppiumConnection.set_certificate_bundle_path(None)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        super().__init__(
            AppiumConnection(command_executor, keep_alive=keep_alive), desired_capabilities, browser_profile, proxy
        )

        if hasattr(self, 'command_executor'):
            self._addCommands()

        self.error_handler = MobileErrorHandler()

        if direct_connection:
            self._update_command_executor(keep_alive=keep_alive)
