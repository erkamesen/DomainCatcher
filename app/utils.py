import time
from functools import wraps
import yaml
from enum import Enum

EMOJIS = {
    "available": "🟢",
    "registered": "🔴",
}


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def get_yaml(filename):
    with open(filename, "r") as stream:
        try:
            conf_file = yaml.safe_load(stream)
            EXTENSIONS = conf_file.get("extensions")
            CHAT_IDS = conf_file.get("chat_ids")
            return EXTENSIONS, CHAT_IDS
        except yaml.YAMLError as exc:
            print(exc)


def message(domain, back_link, domain_pop, abirth, status_com,
            status_net, status_org, status_de, status_ld_registered,
            related_cnobi, changes, whois):
    response = f"""
        Domain Name: {domain}
        Backlink Count: {back_link}
        Domain Pop: {domain_pop}
        Birth Date: {abirth}
        Status ld Registered: {status_ld_registered}
        Related Cnobi: {related_cnobi}
        .com - Status: {EMOJIS.get(status_com)}
        .net - Status: {EMOJIS.get(status_de)}
        .org - Status: {EMOJIS.get(status_net)}
        .de - Status: {EMOJIS.get(status_org)}
        Changes: {changes}
        WHOIS: {EMOJIS.get(whois)}
        """
    return response
