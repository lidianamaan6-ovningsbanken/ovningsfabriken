"""Lokal maskinöversättning med Argos Translate-modeller (CTranslate2). Inget skickas till någon tjänst.
Stöder både modeller med sentencepiece.model och modeller med bpe.model (Moses + subword-nmt)."""
import ctranslate2, os, sys, time

class Model:
    def __init__(self, d, src='en', tgt='xx'):
        self.t = ctranslate2.Translator(d + '/model', device='cpu', inter_threads=1, intra_threads=4)
        if os.path.exists(d + '/sentencepiece.model'):
            import sentencepiece as spm
            self.sp = spm.SentencePieceProcessor(model_file=d + '/sentencepiece.model'); self.bpe = None
        else:
            from sacremoses import MosesTokenizer, MosesDetokenizer, MosesPunctNormalizer
            from subword_nmt.apply_bpe import BPE
            self.sp = None
            self.norm, self.tok, self.detok = MosesPunctNormalizer(lang=src), MosesTokenizer(lang=src), MosesDetokenizer(lang=tgt)
            with open(d + '/bpe.model', encoding='utf-8') as f: self.bpe = BPE(f)
    def enc(self, x):
        if self.sp: return self.sp.encode(x, out_type=str)
        toks = self.tok.tokenize(self.norm.normalize(x), escape=False)
        return self.bpe.segment_tokens(toks)
    def dec(self, toks):
        if self.sp: return self.sp.decode(toks).replace('▁', ' ').strip()
        s = ' '.join(toks).replace('@@ ', '').replace('@@', '')
        return self.detok.detokenize(s.split())

def load(d, src='en', tgt='xx'):
    return Model(d, src, tgt)

def tr(m, texts, bs=32):
    res = m.t.translate_batch([m.enc(x) for x in texts], max_batch_size=bs, beam_size=2, max_decoding_length=512)
    return [m.dec(r.hypotheses[0]) for r in res]

if __name__ == '__main__':
    m = load(sys.argv[1], *(sys.argv[2].split('-') if '-' in sys.argv[2] else ('en', 'xx'))); s = time.time()
    print(tr(m, sys.argv[3:])); print(time.time() - s)
