import ctranslate2, sentencepiece as spm, sys, json, time
def load(d):
    return ctranslate2.Translator(d+'/model', device='cpu', inter_threads=1, intra_threads=4), spm.SentencePieceProcessor(model_file=d+'/sentencepiece.model')
def tr(model, texts, bs=32):
    t, sp = model
    toks = [sp.encode(x, out_type=str) for x in texts]
    res = t.translate_batch(toks, max_batch_size=bs, beam_size=2, max_decoding_length=512)
    return [sp.decode(r.hypotheses[0]).replace('▁',' ').strip() for r in res]
if __name__ == '__main__':
    m = load(sys.argv[1]); s=time.time()
    print(tr(m, sys.argv[2:])); print(time.time()-s)
