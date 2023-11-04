import { MdOutlineNotificationsNone } from 'react-icons/md';

import NotificationModal from './NotificationModal';

export default function Notification_Presenter({ iconSize, showNoti, setShowNoti, setShowTeamApp }) {
  const handleClose = () => {
    setShowNoti(false);
  };
  const handleShow = () => {
    setShowNoti(true);
  };
  return (
    <>
      <MdOutlineNotificationsNone size={iconSize} onClick={handleShow} className="nav-bar-icons" />
      <NotificationModal
        iconSize={iconSize}
        show={showNoti}
        handleClose={handleClose}
        setShowTeamApp={setShowTeamApp}
      />
    </>
  );
}
