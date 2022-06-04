//import "./App.css";
import "./common.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./pages/Login.js";
import MailIndex from "./pages/MailIndex.js";
import Logout from "./pages/Logout.js";

//<Route path="/inbox/" element={<Mails type="inbox" />} />
//<Route path="/inbox/:id/" element={<MailDetail />} />
//<Route path="/sent" element={<Mails type="sent" />} />
//<Route path="/sent/:id/" element={<MailDetail />} />
//<Route path="/archived/" element={<Mails type="archived" />} />
//<Route path="/archived/:id/" element={<MailDetail />} />
//<Route path="/compose/" element={<Compose />} />

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/mail/*" element={<MailIndex />} />
        <Route path="/logout/" element={<Logout />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
