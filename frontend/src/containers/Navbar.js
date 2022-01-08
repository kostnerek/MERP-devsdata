import NavbarLink from "../components/NavbarLink"

import "../styles/Navbar.css"

const Navbar = () => {
    return (
        <div className="navbar">
            <div className="navbar-logo">Magic Events Company</div>
            <div className="navbar-links">
                <NavbarLink direction="/" directionName="Events" />
                <NavbarLink direction="/manage" directionName="Manage reservation" />
            </div>
        </div>
    )
}

export default Navbar