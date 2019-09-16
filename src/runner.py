import PySimpleGUI as sg

from training import *

def simple_runner(sentence, pretrained=False):
    if pretrained is False:
        optimizer, vectorizer, examples, graph = train_network(num_pages=9)
    else:
        with open('/data/saved.dill', 'rb') as f:
            optimizer, vectorizer, examples, graph = dill.load(f)

    example = vectorizer.transform([sentence]).toarray()
    np.append(examples, example)
    examples = add_padding(examples)
    pred = optimizer.predict(example[-1])[0][0]
    print(f'Raw output: {pred:.2f}, Result: {"Pun" if pred > 0.5 else "Not Pun"}')
    confidence = f'{pred * 100 if pred > 0.5 else 100 - (pred * 100):.2f}%'
    sg.ChangeLookAndFeel('Black')
    layout = [
        [sg.Text(f"Sentence: {sentence}", font=('Ubuntu', '18'))],
        [sg.Text(f'Prediction: {"Pun" if pred > 0.5 else "Not Pun"}', font=('Ubuntu', '20'))],
        [sg.Text(f'Confidence: {confidence}', font=('Ubuntu', '18'))],
        [sg.Image(data=graph)],
        [sg.Button('Save network'), sg.Exit()]
    ]
    window = sg.Window(title="Result", layout=layout)
    while True:
        event, values = window.Read()
        if event == "Save network":
            data = (optimizer, vectorizer, examples, graph)
            with open('/data/saved.dill', 'wb') as f:
                dill.dump(data, f)
        elif event is None or event == 'Exit':
            break

    window.Close()

def file_runner(file_path, pretrained=False):
    with open(file_path, 'r') as f:
        data = f.readlines()
    if pretrained is False:
        optimizer, vectorizer, examples, graph = train_network(num_pages=9)
    else:
        with open('/data/saved.dill', 'rb') as f:
            optimizer, vectorizer, examples, graph = dill.load(f)

    inputs = vectorizer.transform(data).toarray()
    inputs = add_padding(inputs)
    outputs = optimizer.predict(inputs)
    for key, value in enumerate(outputs):
        if value == 1:
            print(data[key])


if __name__ == '__main__':
    sg.ChangeLookAndFeel('Black')
    layout = [
        [sg.Text('Use pretrained network?')],
        [sg.Button('Yes'), sg.Button('No')]
    ]
    win = sg.Window('Prompt', layout=layout)
    while True:
        event, values = win.Read()
        if event == 'Yes':
            pretrained=True
            win.Close()
            break
        elif event == 'No':
            pretrained=False
            win.Close()
            break

    simple_runner("To the mathematicians who thought of the idea of zero, thanks for nothing!", pretrained=pretrained)
    # file_runner('/data/Shrek.txt', pretrained=False)
