"""notification."""
import notify2


class notification:
    def send(self, msg=None):
        notify2.init('Host-swicher-notification')
        notif = notify2.Notification(
            "Host-switcher",
            msg
        )
        notif.show()
        pass
