import React, { Component } from "react";
import "../../styles/footer.css"
import { FaGithub, FaInstagram, FaXTwitter } from "react-icons/fa6";


export const Footer = () => (
	<footer className="footer mt-auto p-5 bg-dark text-white d-flex justify-content-between align-items-center">

		<h2 className="mb-0"><strong>PadelZone</strong></h2>

		<div>
			<p className="mb-3 text-center">Cookie Policy · Privacy Policy</p>
			<p className="mb-0">© {new Date().getFullYear()} 4Geeks Academy Final Project · Alejandro, José y Marcos · All right reserved</p>
		</div>

		<div>
			<div className="d-flex gap-3">
				<a href="https://github.com" target="_blank" rel="noopener noreferrer" className="text-light">
					<FaGithub size={24} />
				</a>
				<a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="text-light">
					<FaInstagram size={24} />
				</a>
				<a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="text-light">
					<FaXTwitter size={24} />
				</a>


				<button
					className="btn text-light footer__button--hover"
					onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
				>
					↑
				</button>
			</div>
		</div>
	</footer>
);