import styles from "./styles.module.scss"
import Button from "../Button"
export default function Form({ children }) {
    return <form className={ styles.form }>{ children }</form>
}

Form.Field = function FormField({ children }) {
    return <div className={ styles.field }>{ children }</div>
}

Form.Label = function InputLabel({ children }) {
    return <label className={ styles.label }>{ children }</label>
}

Form.Input = function FormInput({ type, value, onChange}) {
    return <input className={ styles.input } value={ value } onChange={ onChange } type={ type }/>
} 

Form.Button = function FormButton({ children, ...restProps }) {
    return <Button { ...restProps }>{ children }</Button>
} 