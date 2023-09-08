from sentencepiece import SentencePieceProcessor

def main():
    model_path = 'tokenizer.model'
    sp_model = SentencePieceProcessor(model_file=model_path)

    eos_symbol = sp_model.id_to_piece(sp_model.eos_id())
    print(f"End of sequence (EOS) symbol is: {eos_symbol}")

if __name__ == "__main__":
    main()
