from training import *

def simple_runner():
    optimizer, vectorizer, size = train_network(num_pages=9)

    input_string = "How much did the butcher charge for his venison? A buck!"
    example = vectorizer.transform([input_string]).toarray()
    padding = np.zeros(size-np.size(example))
    example = np.append(example, padding)
    pred = optimizer.predict(example)[0][0]
    print(f'Raw output: {pred}, Result: {"Pun" if pred > 0 else "Not Pun"}')
    import PySimpleGUI as sg
    sg.ChangeLookAndFeel('Black')
    layout = [
        [sg.Text(f"Sentence: {input_string}", font=('Ubuntu', '18'))],
        [sg.Text(f'Result: {"Pun" if pred > 0 else "Not Pun"}', font=('Ubuntu', '20'))],
        [sg.Text(f'ReLu output: {pred}', font=('Ubuntu', '18'))],
        [sg.Text(f'Training graph:', font=('Ubuntu', '18'))],
        [sg.Image('/data/graph.png')],
        [sg.Exit()]
    ]
    window = sg.Window(title="Result", layout=layout)
    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        print(event, values)

    window.Close()

if __name__ == '__main__':
    simple_runner()
