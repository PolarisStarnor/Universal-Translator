from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL = AutoModelForSeq2SeqLM.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

def translate(from_text : str, from_lang : str, to_lang : str) -> str:
    from_lang_model = get_language_code(from_lang)
    to_lang_model = get_language_code(to_lang)

    tokenizer = AutoTokenizer.from_pretrained("facebook/mbart-large-50-many-to-many-mmt", src_lang=from_lang_model)

    encoded = tokenizer(from_text, return_tensors="pt")
    generated_tokens = MODEL.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id[to_lang_model])
    out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return out[0]

def get_language_code(abbreviation):
    language_mapping = {
        'ar': 'ar_AR',
        'cs': 'cs_CZ',
        'de': 'de_DE',
        'en': 'en_XX',
        'es': 'es_XX',
        'et': 'et_EE',
        'fi': 'fi_FI',
        'fr': 'fr_XX',
        'gu': 'gu_IN',
        'hi': 'hi_IN',
        'it': 'it_IT',
        'ja': 'ja_XX',
        'kk': 'kk_KZ',
        'ko': 'ko_KR',
        'lt': 'lt_LT',
        'lv': 'lv_LV',
        'my': 'my_MM',
        'ne': 'ne_NP',
        'nl': 'nl_XX',
        'ro': 'ro_RO',
        'ru': 'ru_RU',
        'si': 'si_LK',
        'tr': 'tr_TR',
        'vi': 'vi_VN',
        'zh': 'zh_CN',
        'af': 'af_ZA',
        'az': 'az_AZ',
        'bn': 'bn_IN',
        'fa': 'fa_IR',
        'he': 'he_IL',
        'hr': 'hr_HR',
        'id': 'id_ID',
        'ka': 'ka_GE',
        'km': 'km_KH',
        'mk': 'mk_MK',
        'ml': 'ml_IN',
        'mn': 'mn_MN',
        'mr': 'mr_IN',
        'pl': 'pl_PL',
        'ps': 'ps_AF',
        'pt': 'pt_XX',
        'sv': 'sv_SE',
        'sw': 'sw_KE',
        'ta': 'ta_IN',
        'te': 'te_IN',
        'th': 'th_TH',
        'tl': 'tl_XX',
        'uk': 'uk_UA',
        'ur': 'ur_PK',
        'xh': 'xh_ZA',
        'gl': 'gl_ES',
        'sl': 'sl_SI',
    }

    language_code = language_mapping.get(abbreviation, None)

    if language_code:
        return language_code
    else:
        raise ValueError("Invalid language: " + abbreviation)
