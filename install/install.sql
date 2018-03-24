--
-- PostgreSQL database dump
--

-- Dumped from database version 10.3
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: greetings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.greetings (
    gname "char"[] NOT NULL,
    rating numeric DEFAULT 0 NOT NULL, 
    primary key(gname)
);


--
-- Name: unknown; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.unknown (
    uname "char"[] NOT NULL,
    rating numeric NOT NULL,
    primary key(uname)
);


