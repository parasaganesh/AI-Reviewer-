# Documentation for requests

## data/repos\requests\setup.py
- Lines: 107
- Functions: None
- Classes: None

## data/repos\requests\docs\conf.py
- Lines: 386
- Functions: None
- Classes: None

## data/repos\requests\docs\_themes\flask_theme_support.py
- Lines: 86
- Functions: None
- Classes: FlaskyStyle

## data/repos\requests\src\requests\adapters.py
- Lines: 696
- Functions: _urllib3_request_context, __init__, send, close, __init__, __getstate__, __setstate__, init_poolmanager, proxy_manager_for, cert_verify, build_response, build_connection_pool_key_attributes, get_connection_with_tls_context, get_connection, close, request_url, add_headers, proxy_headers, send, SOCKSProxyManager
- Classes: BaseAdapter, HTTPAdapter

## data/repos\requests\src\requests\api.py
- Lines: 157
- Functions: request, get, options, head, post, put, patch, delete
- Classes: None

## data/repos\requests\src\requests\auth.py
- Lines: 314
- Functions: _basic_auth_str, __call__, __init__, __eq__, __ne__, __call__, __call__, __init__, init_per_thread_state, build_digest_header, handle_redirect, handle_401, __call__, __eq__, __ne__, md5_utf8, sha_utf8, sha256_utf8, sha512_utf8
- Classes: AuthBase, HTTPBasicAuth, HTTPProxyAuth, HTTPDigestAuth

## data/repos\requests\src\requests\certs.py
- Lines: 17
- Functions: None
- Classes: None

## data/repos\requests\src\requests\compat.py
- Lines: 106
- Functions: _resolve_char_detection
- Classes: None

## data/repos\requests\src\requests\cookies.py
- Lines: 561
- Functions: extract_cookies_to_jar, get_cookie_header, remove_cookie_by_name, _copy_cookie_jar, create_cookie, morsel_to_cookie, cookiejar_from_dict, merge_cookies, __init__, get_type, get_host, get_origin_req_host, get_full_url, is_unverifiable, has_header, get_header, add_header, add_unredirected_header, get_new_headers, unverifiable, origin_req_host, host, __init__, info, getheaders, get, set, iterkeys, keys, itervalues, values, iteritems, items, list_domains, list_paths, multiple_domains, get_dict, __contains__, __getitem__, __setitem__, __delitem__, set_cookie, update, _find, _find_no_duplicates, __getstate__, __setstate__, copy, get_policy
- Classes: MockRequest, MockResponse, CookieConflictError, RequestsCookieJar

## data/repos\requests\src\requests\exceptions.py
- Lines: 151
- Functions: __init__, __init__, __reduce__
- Classes: RequestException, InvalidJSONError, JSONDecodeError, HTTPError, ConnectionError, ProxyError, SSLError, Timeout, ConnectTimeout, ReadTimeout, URLRequired, TooManyRedirects, MissingSchema, InvalidSchema, InvalidURL, InvalidHeader, InvalidProxyURL, ChunkedEncodingError, ContentDecodingError, StreamConsumedError, RetryError, UnrewindableBodyError, RequestsWarning, FileModeWarning, RequestsDependencyWarning

## data/repos\requests\src\requests\help.py
- Lines: 134
- Functions: _implementation, info, main
- Classes: None

## data/repos\requests\src\requests\hooks.py
- Lines: 33
- Functions: default_hooks, dispatch_hook
- Classes: None

## data/repos\requests\src\requests\models.py
- Lines: 1039
- Functions: path_url, _encode_params, _encode_files, register_hook, deregister_hook, __init__, __repr__, prepare, __init__, prepare, __repr__, copy, prepare_method, _get_idna_encoded_host, prepare_url, prepare_headers, prepare_body, prepare_content_length, prepare_auth, prepare_cookies, prepare_hooks, __init__, __enter__, __exit__, __getstate__, __setstate__, __repr__, __bool__, __nonzero__, __iter__, ok, is_redirect, is_permanent_redirect, next, apparent_encoding, iter_content, iter_lines, content, text, json, links, raise_for_status, close, generate
- Classes: RequestEncodingMixin, RequestHooksMixin, Request, PreparedRequest, Response

## data/repos\requests\src\requests\packages.py
- Lines: 23
- Functions: None
- Classes: None

## data/repos\requests\src\requests\sessions.py
- Lines: 831
- Functions: merge_setting, merge_hooks, session, get_redirect_target, should_strip_auth, resolve_redirects, rebuild_auth, rebuild_proxies, rebuild_method, __init__, __enter__, __exit__, prepare_request, request, get, options, head, post, put, patch, delete, send, merge_environment_settings, get_adapter, close, mount, __getstate__, __setstate__
- Classes: SessionRedirectMixin, Session

## data/repos\requests\src\requests\status_codes.py
- Lines: 128
- Functions: _init, doc
- Classes: None

## data/repos\requests\src\requests\structures.py
- Lines: 99
- Functions: __init__, __setitem__, __getitem__, __delitem__, __iter__, __len__, lower_items, __eq__, copy, __repr__, __init__, __repr__, __getitem__, get
- Classes: CaseInsensitiveDict, LookupDict

## data/repos\requests\src\requests\utils.py
- Lines: 1086
- Functions: dict_to_sequence, super_len, get_netrc_auth, guess_filename, extract_zipped_paths, atomic_open, from_key_val_list, to_key_val_list, parse_list_header, parse_dict_header, unquote_header_value, dict_from_cookiejar, add_dict_to_cookiejar, get_encodings_from_content, _parse_content_type_header, get_encoding_from_headers, stream_decode_response_unicode, iter_slices, get_unicode_from_response, unquote_unreserved, requote_uri, address_in_network, dotted_netmask, is_ipv4_address, is_valid_cidr, set_environ, should_bypass_proxies, get_environ_proxies, select_proxy, resolve_proxies, default_user_agent, default_headers, parse_header_links, guess_json_utf, prepend_scheme_if_needed, get_auth_from_url, check_header_validity, _validate_header_part, urldefragauth, rewind_body, proxy_bypass_registry, proxy_bypass, get_proxy
- Classes: None

## data/repos\requests\src\requests\_internal_utils.py
- Lines: 50
- Functions: to_native_string, unicode_is_ascii
- Classes: None

## data/repos\requests\src\requests\__init__.py
- Lines: 184
- Functions: check_compatibility, _check_cryptography
- Classes: None

