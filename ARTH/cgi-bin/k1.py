#!/bin/python3
print("content-type:text/plain\n")



@app.route("/imagesubmit", methods=['GET', 'POST'])
def imagesubmit():
    if request.form.get('submit') == 'submit':
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('viewimage'))
    return render_template('yourUploadImage.html', form=form )
