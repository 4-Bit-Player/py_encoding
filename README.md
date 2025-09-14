

# Small encoding package


Features: 
- 
- En-/Decode most basic python types to strings and back!
   - Lists, Dicts, Tuples, Sets, Str, Int, Float, Bools, None
- Almost any nested combination is supported.
- "Blazingly fast" decoding and fast encoding
- Support for any valid key values for dictionaries from the supported types
- Smaller resulting size \
  (downside: not really readable/editable strings)


Currently known issues:
- 
- When encoding strings the ' " ' char followed by an unescaped '\3' char will lead to errors.
- Bytes and Custom Types are currently not supported (though I will add support for bytes soon)


Made in pure python and somehow faster at decoding than literal_eval.


Faster encoding than the uncached build in str() as well. \
Though unfortunately not as fast when its cached.






