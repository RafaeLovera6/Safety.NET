import React, { useState, useCallback } from "react";
import { Link, useHistory } from "react-router-dom";
import * as Icons from "react-icons/fa";
import "./Navbar.css";
import { navItems } from "./NavItems";
import Button from "./Button";
import Dropdown from "./Dropdown";

export const Navbar = () => {
  const [dropdown, setDropdown] = useState(false);
  const history = useHistory();
  const handleOnClick = useCallback(
    () => history.push("/admin_login"),
    [history]
  );

  return (
    <nav className="navbar">
      <Link to="/landing_page" className="navbar-logo">
        <h2>SecureEventApp-SEA</h2>
      </Link>
      <ul className="nav-items">
        {navItems.map((item) => {
          if (item.title === "Events") {
            return (
              <li
                key={item.id}
                className={item.cName}
                onMouseEnter={() => setDropdown(true)}
                onMouseLeave={() => setDropdown(false)}
              >
                <Link to={item.path}>{item.title}</Link>
                {dropdown && <Dropdown />}
              </li>
            );
          }
          return (
            <li key={item.id} className={item.cName}>
              <Link onChange={handleOnClick} to={item.path}>
                {item.title}
              </Link>
            </li>
          );
        })}
      </ul>
      <Button />
    </nav>
  );
};
