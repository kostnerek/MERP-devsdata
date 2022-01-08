import { Link } from "react-router-dom";

const NavbarLink = (props) => {
	return (
		<Link to={`${props.direction}`} className="navbar-link">
			{props.directionName}
		</Link>
	);
};

export default NavbarLink;
