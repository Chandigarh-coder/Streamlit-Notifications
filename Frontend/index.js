import React from "react";
import { Streamlit } from "streamlit-component-lib";

class PushNotification extends React.Component {
  componentDidMount() {
    if (Notification.permission === "granted") {
      new Notification(this.props.title, {
        body: this.props.body,
        icon: this.props.icon,
      });
    } else {
      Notification.requestPermission().then((permission) => {
        if (permission === "granted") {
          new Notification(this.props.title, {
            body: this.props.body,
            icon: this.props.icon,
          });
        }
      });
    }
  }

  render() {
    return null;
  }
}

export default PushNotification;
